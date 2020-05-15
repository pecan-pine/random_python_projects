import re, pyperclip
phone = re.compile(r'(\d{3})-(\d{3}-\d{4})')
try:
    print(phone.search(pyperclip.paste()).groups())
except AttributeError:
    print('no phone number found')