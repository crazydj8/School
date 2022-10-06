# Project on data file handling

import os                   

def add():                  
    global txt
    txt = ""
    rno = int(input("Enter the Roll. No.:"))
    nm = input("Enter the name:")
    pct = int(input("Enter the Percentage:"))
    txt = str(rno) + "," + nm + "," + str(pct) + "\n"
    
def prt():                  
    size = os.path.getsize(file)
    if size == 0:
        print("File Empty")
    else:
        f1.seek(0)
        str = " "
        while str:
            str = f1.readline()
            if str == "":
                break
            print(str)
        
def search(x):                  
    size = os.path.getsize(file)
    if size == 0:
        print("File Empty")
    else:
        f1.seek(0)
        str =  " "
        while str:
            str = f1.readline()
            if str == "":
                print("Roll No. not found")
                break
            l = str.split(",")
            if int(l[0]) == x:
                print(str)
                break
                
def delete(x):                  
    size = os.path.getsize(file)
    if size == 0:
        print("File Empty")
    else:
        global f1
        f1.seek(0)
        str1 =  " "
        l1 = []
        while str1:
            str1 = f1.readline()
            if str1 == "":
                break
            l = str1.split(",")
            l1.append(l)
        curlen = len(l1)
        for i in range(0, len(l1)):
            item = ""
            if int(l1[i][0]) == x:
                item = str(l1[i][0]) + "," + l1[i][1] + "," + str(l1[i][2])
                l1.pop(i)
                break
        newlen = len(l1)
        if curlen == newlen:
            print("Roll No. not found")
        else:   
            f1.close()
            f1 = open(file, "w")
            record = ""
            for i in range(0, len(l1)):
                record = str(l1[i][0]) + "," + l1[i][1] + "," + str(l1[i][2])
                f1.write(record)
            print("Values:", item, "were deleted successfully") 
            f1.close()
            f1 = open(file, "a+")
            
def modify(x, a, b):                    
    size = os.path.getsize(file)
    if size == 0:
        print("File Empty")
    else:
        global f1
        f1.seek(0)
        str1 =  " "
        l1 = []
        condition = 1
        while str1:
            str1 = f1.readline()
            if str1 == "":
                break
            l = str1.split(",")
            l1.append(l)
        for i in range(0, len(l1)):
            item = ""
            if int(l1[i][0]) == x:
                condition = 0
                item1 = str(l1[i][0]) + "," + l1[i][1] + "," + str(l1[i][2])
                l1[i][1] = a
                l1[i][2] = str(b) + "\n"
                item2 = str(l1[i][0]) + "," + l1[i][1] + "," + str(l1[i][2])
        if condition == 1:
            print("Roll. no not found")
        else:
            f1.close()
            f1 = open(file, "w")
            record = ""
            for i in range(0,len(l1)):
                record = str(l1[i][0]) + "," + l1[i][1] + "," + str(l1[i][2])
                f1.write(record)
            print("Values:", item1, "were modified successfully into", item2) 
            f1.close()
            f1 = open(file, "a+")
    
file = "F:\\School\\Online classes Python\\08 August\\August week 1\\files\\projectDFH.txt"                 
txt = ""
f1 = open(file, "a+")                   #made by Akshat Aryan

while True:                 
    print("Your choices are: \n1. Add \n2. Edit \n3. Search \n4. Delete \n5. Print \n6. Exit")
    x = int(input("Enter option number:"))
    if x == 1:                  
        while True:
            add()
            print("Data to be added is:", txt)
            f1.write(txt)
            print("Data added successfully")
            ch = input("Do you want to add more data?(yes/no)")
            if ch == "no":
                break
        f1.close()
        f1 = open(file, "a+")
    
    elif x == 2:                    
        a = int(input("Enter the Roll No. you have to modify:"))
        b = input("Enter new name:")
        c = input("Enter new percentage:")
        modify(a, b, c)
    
    elif x == 3:                    
        a = int(input("Enter the Roll No. you have to search for:"))
        search(a)
        
    elif x == 4:                    
        a = int(input("Enter the Roll No. you have to delete:"))
        delete(a)
        
    elif x == 5:                    
        prt()
    
    elif x == 6:                    
        break

f1.close()                 