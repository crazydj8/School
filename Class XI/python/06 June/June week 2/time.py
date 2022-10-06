# read time in seconds and display time in hours, minutes and seconds

s = int(input("Enter the time in seconds: "))

h = s // 3600
a = s % 3600
m = a // 60
b = a % 60

print ("Time= ", h, "Hours, ", m, "Minutes, ", b, "Seconds")