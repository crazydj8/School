#Write a function called matches that takes two strings as arguments and returns how many matches there are between the strings.
#A match is where the two strings have the same character at the same index. For instance, 'python' and 'path' match in the ﬁrst, third, and fourth characters, so the function should return 3.

def matches(a, b):
    suma = 0
    x = len(a)
    y = len(b)
    if x <= y:
        for i in range(0, x):
            if a[i] == b[i]:
                suma = suma + 1
    else:
        for i in range(0, y):
            if a[i] == b[i]:
                suma = suma + 1    
    return(suma)
                
                
x = "aslow"
y = "allow"

print(matches(x, y))


