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
        highlight_text.append(highlight_sentence)

even_indices = [num for num in range(0, len(highlight_text)) if num % 2 == 0]
odd_indices = [num for num in range(0, len(highlight_text)) if num % 2 != 0]

#print("length of highlight_text", len(highlight_text))
#print("Odd indices", odd_indices)
#print("Even indices", even_indices)

highlight_text_starts = [highlight_text[index] for index in even_indices]
highlight_text_ends = [highlight_text[index] for index in odd_indices]

# Create the new list with "blahblahblah" between corresponding elements
txt1 = "Can you summarize the portion of the article between the text \""
txt2 = "\" and \""
txt3 = "\"? Please put the summary in markdown syntax, suitable for compilation to a beamer slide presentation to be compiled with pandoc. Also, do not include unicode characters, please put everything in LaTeX syntax. Also, do not include the YAML front matter."
new_list = [txt1 + highlight_text_starts[i] + txt2 + highlight_text_ends[i] + txt3 for i in range(len(highlight_text_starts))]

#print(new_list)
with open("text_prompts.txt", "w") as file:
    file.write("\n\n".join(new_list))
