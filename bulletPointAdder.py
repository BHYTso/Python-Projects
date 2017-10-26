#Adding Bullets to Wiki Markup

#! python3
# bulletPointAdder.py - Adds Wiki bullet points to the start
# of each line of text on the clipboard.

'''
1. Paste text from the clipboard
2. Do something to it
3. Copy the new text to the clipboard
'''

pip install -U pip
sudo idle3 install pyperclip

import pyperclip
text = pyperclip.paste()        #1

#TODO: Separate lines and add stars.   #2

#Separate lines and add stars.

lines = text.split('\n')
for i in range(len(lines)):     #loop through all indexes in the "lines" list
    lines[i] = '*' + lines[i]   #add star to each string in "lines" list

text = '\n'.join(lines)

pyperclip.copy(text)            #3
