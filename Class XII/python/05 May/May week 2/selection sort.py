# write a program to sort diagonal elements of square matrix using selection sort

m1 = [[7, 2, 3], [4, 6, 3], [2, 3, 9]]

print("Your matrix is:")
for i in range(0, len(m1)):
    for j in range(0, len(m1)):
        print(m1[i][j], end = " ")
    print("")
    
def sorta(m1):
    for i in range(0, len(m1)):
        small = m1[i][i]
        pos = i
        for j in range(i+1, len(m1)):
            if m1[j][j] < small:
                small = m1[j][j]
                pos = j
        
        x = m1[i][i]
        m1[i][i] = m1[pos][pos]
        m1[pos][pos] = x
        
    for i in range(0, len(m1)):
        for j in range(0, len(m1)):
            print(m1[i][j], end = " ")
        print("")
print("Your sorted matrix is:")        
sorta(m1)