# read and check if a number is palindrome number
# a palindrome number is a number which is the same written backwards

a = int(input("Enter your number:"))

if a < 10:
    print ("Please enter a number greater than 9 and try again")

else:
    num = 0
    b = a

    while b > 0:
        r = b % 10
        b = b // 10
        num = 10 * num + r

    if num == a:
        print (a, "Is a palindrome number.")
    else:
        print (a, "Is not a palindrome number.")
