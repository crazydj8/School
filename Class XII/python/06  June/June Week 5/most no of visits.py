# a list represents the date of visits of each patient of a clinic. find the patient with most visits


l1 = [[2, 6], [3, 10], [15], [23], [1, 8, 15, 19, 22], [14]]

def most(l1):
    large = [l1[0]]
    for i in range(1, len(l1)):
        if len(l1[i]) > len(large[0]):
            large = []
            large.append(l1[i])
        elif len(l1[i]) == len(large[0]):
            large.append(l1[i])
    
    return(large)
    
print(most(l1))