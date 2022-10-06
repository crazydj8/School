import csv

stu = []
fields = ["roll no", "name", "percentage"]
file = "D:\\Study\\School\\Online classes Python\\09 September\\September week 3\\files\\new.csv"
def add():
    while True:
        rec = []
        rec.append(int(input("Enter Roll. no.:")))
        rec.append(input("Enter name:"))
        rec.append(int(input("Enter percentage:")))
        stu.append(rec)
        ch = input("Continue adding more records?(y/n):")
        if ch == "n":
            break

while True:
    print("Your choices are: \n1. Add \n2. Search \n3. Print \n4. Delete \n5. Exit")
    x = int(input("Enter option number:"))
    if x == 1:
        add()
        with open(file, 'a', newline = "") as adddata:
            w = csv.writer(adddata)
            w.writerow(fields)
            w.writerows(stu)
    
    if x == 2:
        x = input("Enter the roll no. to search:")
        c = 0
        with open(file, 'r') as searchdata:
            r = csv.reader(searchdata)
            for i in r:
                if i[0] == x:
                    c = 1
                    print("Found:", i)
            if c == 0:
                print("Not Found")
    
    if x == 3:
        with open(file, 'r') as printdata:
            r = csv.reader(printdata)
            for i in r:
                print (i)
                
    if x == 4:
        x = input("Enter the roll no. to delete:")
        c = 0
        newlist = []
        with open(file, 'r') as delete:
            r = csv.reader(delete)
            for i in r:
                if i[0] == x:
                    c = 1
                if i[0] != x:
                    newlist.append(i)
                
            if c == 0:
                print("Record not found")
            else:
                with open(file, 'w', newline = "") as deladd:
                    w = csv.writer(deladd)
                    w.writerow(fields)
                    w.writerows(newlist)
                    
    if x == 5:
        break
                
            
            
            