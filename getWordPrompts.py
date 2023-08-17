import fitz
import sys

if len(sys.argv) != 2:
    print("Usage: python script_name.py <pdf_filename>")
    sys.exit(1)

pdf_filename = sys.argv[1]

doc = fitz.open(pdf_filename)

# List to store all the highlighted texts
highlight_text = []

# Iterate over each page of the document
for page in doc:
    # Get all the words on the page
    words = page.get_text_words()

    # Get the highlight regions on the page
    highlights = [annot for annot in page.annots() if annot.type[0] == 8]

    # Process each highlight and extract the corresponding text
    for highlight in highlights:
        highlight_rect = highlight.rect
        highlight_words = [w for w in words if fitz.Rect(w[:4]).intersects(highlight_rect)]
        highlight_sentence = " ".join(w[4] for w in highlight_words)
        highlight_sentence = " ".join(highlight_sentence.split()[1:-1])  # Remove first and last words
        highlight_text.append(highlight_sentence)

doc.close()  # Close the PDF document

# Print the list of highlighted texts
# for index, sentence in enumerate(highlight_text, start=1):
#    print(f"{index}. {sentence}")

# Create a single string called "phrases" with semicolon-separated elements
phrases = ";".join(highlight_text)

# Print the concatenated phrases
# print(phrases)

# Edit this prompt if you find something that works better:
txt1 = "I have a list of words/phrases separated by semicolons. Can you provide the definitions of these words/phrases for me (a few sentences per word/phrase)? Here is the list: "
with open("jargon_prompts.txt", "w") as file:
    file.write(txt1 + phrases)
