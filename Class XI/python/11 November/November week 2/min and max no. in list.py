'''read a list of integers and find the minimum and maximum along with 
index'''

list = eval(input("Enter your list(Elements separated by a ','):"))

y = len(list)

for i in range(0, y):
    if i == 0:
        sml = list[i]
        lrg = list[i]
        
    if list[i] > lrg:
        lrg = list[i]
        y = i
        
    elif list[i] < sml:
        sml = list[i]
        x = i
        
print ("Smallest number:", sml, "Position:", x)
print ("Largest number:", lrg, "Position:", y)