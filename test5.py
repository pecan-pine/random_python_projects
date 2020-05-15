def listwords(l):
    newlist = []
    for x in l:
        if x == "[" or x == "]":
            continue
        elif l.index(x) <= len(l)-3:
            newlist.append(x)
        elif l.index(x) == len(l)-2:
            newlist.append( ' and ')
            newlist.append(x)
            newlist.append('.')
    return print(''.join(newlist))

word = None

while word != "stop":
    word = list(input("Type in a list, or type \'stop\' to quit."))
    listwords(word)



