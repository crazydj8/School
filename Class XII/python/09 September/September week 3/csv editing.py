# csv file handling

import csv
with open("D:\\Study\\School\\Class XII\\09 September\\September week 3\\files\\csv editing.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
file = open("D:\\Study\\School\\Class XII\\09 September\\September week 3\\files\\csv editing.csv", "r")
for line in file:
    print(line)