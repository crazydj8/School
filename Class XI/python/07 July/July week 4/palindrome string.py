# check whether a string is a palindrome number:

str = input("Enter the string:")

x = len(str)
p = 0

for i in range(0, x):
    p = p - 1
    if (str[i]) == (str[p]):
        a = 1
    else:
        a = 0
        
if a == 1:
    print ("yes, it is a palindrome string.")
else:
    print ("no, it is a not a palindrome string.")