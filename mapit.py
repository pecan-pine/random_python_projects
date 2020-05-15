#https://www.google.com/maps/place/2543+Kincaid+St,+Eugene,+OR+97405/
import sys,webbrowser,pyperclip

if len(sys.argv) > 1:
    del sys.argv[0]
    webbrowser.open('https://www.google.com/maps/place/' + '+'.join(sys.argv))
    #'+'.join(address)
else:
    address = pyperclip.paste()
    address = address.split(' ')
    webbrowser.open('https://www.google.com/maps/place/' + '+'.join(address))

