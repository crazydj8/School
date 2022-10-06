# write a program to copy contents of  a source file to destination file if either dont exist, abandon operation

import os

if os.path.exists("F:\\School\\Online classes Python\\08 August\\August week 1\\files\\source.txt"):
    f1 = open("F:\\School\\Online classes Python\\08 August\\August week 1\\files\\source.txt", "r")
    if os.path.exists("F:\\School\\Online classes Python\\08 August\\August week 1\\files\\destination.txt"):
        a = input("Do you want to overwrite the file?(yes/no)")
        if a == "yes":
            f2 = open("F:\\School\\Online classes Python\\08 August\\August week 1\\files\\destination.txt", "w")
            str = f1.read()
            f2.write(str)
            print("file overwrite successful")
            f2.close()
        else:
            print("You chose not to overwite. the process will be abandoned.")
            f1.close()
    else:
        print("Destination file not found. the process will be abandoned.")
        f1.close()
else:
    print("Source file not found. the process will be abandoned.")
    