import fitz  # PyMuPDF
import os
from openai import OpenAI

# -------------------------------
# Ask for input interactively
# -------------------------------
pdf_filename = input("Enter the name of the PDF file (e.g., document.pdf): ").strip()
prompts_filename = input("Enter the name of the text file containing prompts (e.g., prompts.txt): ").strip()

# -------------------------------
# Load OpenAI client
# -------------------------------
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -------------------------------
# Step 1: Extract highlight pairs from PDF
# -------------------------------
doc = fitz.open(pdf_filename)
highlight_rects = []
highlight_texts = []

for page in doc:
    words = page.get_text_words()
    annots = page.annots()
    if annots:
        highlights = [annot for annot in annots if annot.type[1] == "Highlight"]
        for highlight in highlights:
            rect = highlight.rect
            highlight_words = [w for w in words if fitz.Rect(w[:4]).intersects(rect)]
            text = " ".join(w[4] for w in sorted(highlight_words, key=lambda x: (x[1], x[0])))
            highlight_rects.append(rect)
            highlight_texts.append(text)

highlight_pairs = list(zip(highlight_texts[::2], highlight_texts[1::2]))

# -------------------------------
# Step 2: Extract text between highlight regions
# -------------------------------
section_texts = []
for i in range(0, len(highlight_rects), 2):
    if i + 1 >= len(highlight_rects):
        break
    start_rect = highlight_rects[i]
    end_rect = highlight_rects[i + 1]
    collected_text = []

    for page in doc:
        blocks = page.get_text("blocks")
        for block in blocks:
            rect = fitz.Rect(block[:4])
            if rect.intersects(start_rect) or rect.intersects(end_rect) or (
                rect.y0 > start_rect.y1 and rect.y1 < end_rect.y0
            ):
                collected_text.append(block[4])
    section_texts.append("\n".join(collected_text).strip())

# -------------------------------
# Step 3: Load prompts
# -------------------------------
with open(prompts_filename, "r") as f:
    prompts = f.read().strip().split("\n\n")

num_pairs = min(len(prompts), len(section_texts))

# -------------------------------
# Step 4: Send to GPT
# -------------------------------
with open("responses.txt", "w") as out:
    for i in range(num_pairs):
        prompt = prompts[i]
        section = section_texts[i]

        print(f"Sending prompt {i+1}...")

        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an academic assistant that summarizes sections of a PDF."},
                    {"role": "user", "content": f"Here is a section of the PDF:\n\n{section}\n\n{prompt}"}
                ],
                temperature=0.7
            )
            reply = response.choices[0].message.content.strip()
            out.write(f"--- Response to Prompt {i+1} ---\n")
            out.write(reply + "\n\n")
        except Exception as e:
            print(f"Error on prompt {i+1}: {e}")
            out.write(f"--- Error on Prompt {i+1}: {e} ---\n\n")

