# write a function check that recieves a string and returns the number of upper case characters, lower case characters and digits, puts count in a dictionary and returns a dictionary.

def check(str1):
    sumu = 0
    suml = 0
    sumd = 0
    for i in str1:
        if i.isupper():
            sumu = sumu + 1
        elif i.islower():
            suml = suml + 1
        elif i.isdigit():
            sumd = sumd + 1
            
    dict = {"Upper":sumu, "Lower":suml, "Digits":sumd}
    return (dict)
    
str1 = input("Enter the string:")

print(check(str1))