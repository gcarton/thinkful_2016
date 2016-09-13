import sys

n = int(sys.argv[1])

if len(sys.argv[1])<2:
    n = input

for n in range(1,n+1):
    if n % 15 == 0:
        print ("fizzbuzz")
    elif n % 5 == 0:
        print ("buzz")
    elif n % 3 == 0:
        print ("fizz")
    else:
        print (n)
        