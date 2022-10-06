''' read a list and an elemenet to be searched and count the 
number of occurances of the element in the list'''

list = eval(input("Enter your list(Elements separated by a ','):"))

text = input("Enter the pattern to search for:")

a = len(list)
suma = 0

for i in range(0, a):
    if str(lst3[i]) == text:
        suma = suma + 1
        
print("Occurances=", suma)
