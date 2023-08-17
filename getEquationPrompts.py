import fitz
import sys

if len(sys.argv) != 2:
    print("Usage: python script_name.py <pdf_filename>")
    sys.exit(1)

pdf_filename = sys.argv[1]

doc = fitz.open(pdf_filename)

# doc = fitz.open("phan2022simple.pdf")

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
        highlight_text.append(highlight_sentence)


txt1 = "I am going give you a list of sentences from this pdf. Immediately after each of these sentences there is an equation or a system of equations in the pdf. Can you extract all of those equations and put them in LaTeX syntax? The list of sentences is: "
txt2 = ', '.join(['"' + s + '"' for s in highlight_text])
txt3 = ". Remember to put your response in LaTeX syntax because I am going to compile what you produce in LaTeX. Put all of the results into a single code chunk that I can copy."

with open("equation_prompts.txt", "w") as file:
    file.write(txt1 + txt2 + txt3)
