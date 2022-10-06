'''read 2 lists and add them into a third list and count the number of
occurances of any element'''

list = eval(input("Enter your list(Elements separated by a ','):"))
lst2 = eval(input("Enter your list(Elements separated by a ','):"))

lst3 = list + lst2

text = input("Enter the pattern to search for:")

a = len(lst3)
suma = 0

for i in range(0, a):
    if str(lst3[i]) == text:
        suma = suma + 1
        
print("Occurances=", suma)

