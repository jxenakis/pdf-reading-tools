# PDF Interrogration Tools

These are a few of my tools that facilitate PDF interrogration with ChatGPT. To use, activate the virtual environment `cliprompt`.

## getTextPrompts.py

Define chunks of text by highlighting, for each chunk, a starting section and and ending section (these can be parts of lines of the pdf, or multiple contiguous lines of the pdf). Each chunk must have exactly two highlighted pieces associated with it; there must therefore be an even number of sections highlighted in the pdf. Then, run from the commandline:

    python3 getTextPrompts.py <filename>

where <filename> is the name of your pdf (including the .pdf extension).

A file called `text_prompts.txt` that contains a set of prompts will be created in the directory. Each prompt is designed to ask for a short summary of its associated chunk. You should play with the sizes of the chunks to optimize the pdf summary. 
<!-- You must have the AskYourPDF plugin installed in GPT-4 (and have given GPT the doc_id for you pdf) for this to work.-->



## pdfPrompt.py

This script takes the pdf and the text file of prompts and outputs the summaries of each chunk in a text file called `responses.txt`. Run this from the commandline:

    python3 pdfprompt.py

and you will be prompted to enter the name of the .pdf and your file of prompts (that you probability created with getTestPrompts.py)


## getWordPrompts

Highlight words or phrases that you want defined in a pdf that resides in the same directory as getWordPrompts.py. Then run from the commandline:

   python3 getWordPrompts.py <filename>

where <filename> does not include the .pdf extension.

A file that contains a GPT prompt will be created in the directory.

## getEquationPrompts

Highlight some text immediately before any equations you want to extract and run from the commandline:

   python3 getEquationPrompts.py <filename>

where <filename> does not include the .pdf extension.

A file that contains a GPT prompt will be created in the directory. 
<!-- You must have the AskYourPDF plugin installed in GPT-4 (and have given GPT the doc_id for you pdf) for this to work. -->

