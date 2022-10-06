import pickle
list = []

while True:
    roll = input("Enter Roll. no.:")
    sname = input("Enter name:")
    student = {"roll":roll, "name":sname}
    list.append(student)
    ch = input("Continue adding more records?(y/n):")
    if ch == "n":
        break

f1 = "H:\\School\\Online classes Python\\10 October\\October week 2\\files\\student.dat"

file = open(f1, "wb")
pickle.dump(list,file)
file.close()

#read binary file
file = open(f1, "rb")
list = pickle.load(file)
print(list)
file.close()

#search
name = input("Enter the name you want to search for:")
file = open(f1, "rb")
list = pickle.load(file)
file.close()

found = 0
for x in list:
    if name in x["name"]:
        found = 1
print ("Found in binary file" if found == 1 else "Not found")

#update
name = input("Enter the name you want to update:")
file = open(f1, "rb+")
list  = pickle.load(file)
found = 0
for x in list:
    if name in x["name"]:
        found = 1
        x["name"] = input("Enter new name:")
        
if found == 1:
    file.seek(0)
    pickle.dump(list, file)
    print("Record updated")
else:
    print("Name doesnt exist")
file.close()
file = open(f1, "rb")
list = pickle.load(file)
print(list)
file.close()

#delete

name = input("Enter the name you want to delete:")
file = open(f1, "rb+")
list  = pickle.load(file)

found = 0
lst = []
for x in list:
    if name not in x["name"]:
        lst.append(x)
    else:
        found = 1
        
if found == 1:
    file.seek(0)
    pickle.dump(lst, file)
    print("Record Deleted")
else:
    print("Name not found")
file.close()
file = open(f1, "rb")
list = pickle.load(file)
print(list)
file.close()

    
