# enter numbers and find its average

a = int(input("Enter the number of numbers to find average of:"))
s = 0

for n in range(0, a):
    n = int(input("Enter number:"))
    s = s + n

avg = s / a
print ("Average=", avg)
