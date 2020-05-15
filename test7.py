birthdays = {'Steph':'November 18', 'Smoop': 'November 8', 'Jude':'October 28'}

while True:
    print('enter a name, or blank to quit:')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(name+'\'s birthday is ' + birthdays[name])
    else:
        print('I do not have birthday information for this person. What is their birthday?')
        date = input()
        birthdays[name] = date
        print('The database has been updated')