#write a program that generates  series using function that takes first and last values of series and generates 4 terms that ar equidistant eg. 2 nos passed are 1 and 7, then series is 1 3 5 7

def ap(x, y):
    ap = [x]
    for j in range(1, 3):
        a = x + (j * (y - x) / 3)
        ap.append(a)
    ap.append(y)
    return(ap)
    
a = int(input("Enter lower limit:"))
b = int(input("Enter upper limit:"))

print(ap(a, b))
    