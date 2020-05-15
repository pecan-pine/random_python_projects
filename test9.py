import pyperclip
text = pyperclip.paste()

#separate lines and add stars

lines = text.split('\n')
for line in lines:
    lines[lines.index(line)] = '*'+line

text = '\n'.join(lines)
pyperclip.copy(text)
print(pyperclip.paste())

