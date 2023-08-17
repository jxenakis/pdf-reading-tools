# PDF Interrogration Tools

These are a few of my tools that facilitate PDF interrogration with GPT-4. The tools create prompts that can be pasted directly into GPT-4 when using, for example, the AskYourPDF plugin, or into Microsoft Edge, for which the AI assistant is built on GPT-4. In subsequent versions of these tools, the cutting and pasting will be automated (I need API access first). 

## getWordPrompts

Highlight words or phrases that you want defined in a pdf that resides in the same directory as getWordPrompts.py. Then run from the commandline:

python3 getWordPrompts.py filename

where filename does not include the .pdf extension.

A file that contains a GPT prompt will be created in the directory. This can be used the free GPT-3.5.

## getEquationPrompts

Highlight some text immediately before any equations you want to extract and run from the commandline:

python3 getEquationPrompts.py filename

where filename does not include the .pdf extension.

A file that contains a GPT prompt will be created in the directory. You must have the AskYourPDF plugin installed in GPT-4 (and have given GPT the doc_id for you pdf) for this to work.

## getTextPrompts

Define chunks of code by highlighting, for each chunk, a starting section and and ending section (these bits can be parts of lines of the pdf, or multiple contiguous lines of the pdf). Each chunk must have exactly two highlighted pieces associated with it; there must therefore be an even number of sections highlighted in the pdf.

Run from the commandline:

python3 getTextPrompts.py filename

where filename does not include the .pdf extension.

A file that contains a set of GPT prompt will be created in the directory. Each prompt is designed to ask for a short summary it's associated text chunk. You can play with the sizes of the chunks to optimize the pdf summary. You must have the AskYourPDF plugin installed in GPT-4 (and have given GPT the doc_id for you pdf) for this to work.
