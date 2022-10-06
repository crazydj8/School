'''initialize a tuple to store marks of 3 children in 5 subjects. create 
another tuple to store total marks of each child in all subjects and 
print the highest score)'''

# marks = ((phys, chem, maths, comp, eng))

marks = ((70, 65, 85, 85, 60,), (80, 85, 90, 95, 80,), (60, 75, 100, 80, 80,), )
t1 = tuple()
x = len(marks) 

for i in range(0, x):
    a = marks[i][0]+marks[i][1]+marks[i][2]+marks[i][3]+marks[i][4]
    t1 = t1 + (a, )
    
print ("Highest marks=", max(t1))