#ask for input till entered q, capitalize each word of string

str2 = ""

while True:
    str1 = input("Enter your string:")
    if str1 != "q":
        str2 = str1.swapcase() 
        print (str2)
    else:
        break