''' define a tuple of a pair of ten countries and their capitals. read a
country or a capital from the user display the corresponding capital or 
country'''

t = (("India", "Delhi",), ("Japan", "Tokyo",), ("China", "Beijing",), ("Ireland", "Dublin",), ("Germany", "Berlin",), ("Russia", "Moscow",), ("France", "Paris",), ("Spain", "Madrid",), ("Italy", "Rome",), ("Canada", "Ottawa",),)
x = len(t)
name = input("Enter the name of a country or a capital:")

for i in range(0, x):
    if t[i][0] == name:
        print ("Country=", t[i][0], "Capital=", t[i][1])
        break
    elif t[i][1] == name:
        print ("Country=", t[i][0], "Capital=", t[i][1])
        break
    else:
        print ("No Country or Capital found")
        break