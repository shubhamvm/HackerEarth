'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
a = input()
l =list()
b = False
for n in a: 
    if n == "G":
        l.append("C")
    elif n == "C":
        l.append("G")
    elif n == "T":
        l.append("A")
    elif n == "A":
        l.append("U")
    else :
        print("Invalid Input")
        b = True
        break
if b == False:
    for i in l:
        print(i,end="")
