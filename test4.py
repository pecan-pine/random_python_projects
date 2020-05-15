import sys
def collatz(number):
    if number % 2:
        return 3*number + 1
    else:
        return number//2
start = input('give a number: ')
try:
    start = int(start)
except ValueError:
    print('please enter a number')
    sys.exit()
while start != 1:
    start = collatz(start)
    print(start)