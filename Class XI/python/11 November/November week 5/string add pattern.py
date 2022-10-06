''' insert a pattern in a string at the specified position'''

str1 = input("Enter your string:")
text = input("Enter the pattern to insert:")
pos = int(input("Enter the position to insert the pattern:"))

str1 = str1[:pos] + text + str1[pos:]
print (str1)