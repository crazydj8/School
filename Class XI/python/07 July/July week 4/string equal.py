# read two strings of same length and check if same or not

str1 = input("Enter first string:")
str2 = input("Enter first string:")

x = len(str1)
y = len(str2)

if x == y:
    for i in range(0, x):
        if str1[i] == str2[i]:
            a = 1
        else:
            a = 0
            break
            
    if a == 1:
        print ("strings are Equal")
    else:
        print("strings are Unequal")
else:
    print ("please enter strings of same length")
    
