#Python Project 2019 - Akshat and Merril
from collections import Counter

'''Measures of central tendency for grouped and discrete data'''

print ("Data Type:")
print ("1. Discrete Data")
print ("2. Grouped Data")
condition = 1
#condition that input can only be 1 or 2
while condition == 1:
    data = int(input("Enter the data type you want to input(1 or 2):"))
    if data == 1:
        condition = 0
    elif data == 2:
        condition = 0
    else:
        print ("Please input a number from the following numbers = (1, 2)")

#discrete data
if data == 1:
    print("You have selected Discrete data:")
    while condition == 0:
    #number of obs cannot be less than 1
        n = int(input("Please input number of observations:"))
        if n > 0:
            condition = 1
        else:
            print ("Please input a valid total (n>0)")
    l_obs = []
    freq_table = []
    data_table = []
    freq = 0
    for obs in range(0, n):
        ob1 = int(input("Enter your observations:"))
        l_obs.append(ob1)

    freq_dict = Counter(l_obs)
    x = freq_dict.keys()
    y = list(freq_dict.keys())
    k = 0
    
    for i in x:
    #first append obs and freq, then append list of pairs in another list
        freq_table.append(y[k])
        freq_table.append(freq_dict[i])
        data_table.append(freq_table)
        k = k + 1
        freq_table = []
    print ("Your frequency table is[Observation , Frequency]:")
    print (data_table)
    
    if n == 1:
    #if there is only one observation
        print ("The Mean is=", data_table[0][1])
        print ("The Mode is=", data_table[0][1])
        print ("The Median is=", data_table[0][1])
    
    else:    
        #mean
        sig_fi = n #total no. of obs
        sum_obs = 0
        
        for i in range(0, len(data_table)):
            sum_obs = sum_obs + data_table[i][0]*data_table[i][1]
        mean = sum_obs / sig_fi
        print ("The mean is=", mean)
        
        #mode
        #there can be more than one mode
        mode_list = []
        for i in range(0, len(data_table)):
            if i == 0:
                lrg = data_table[i][1]
            
            if data_table[i][1] > lrg:
                mode_list = []
                lrg = data_table[i][1]
                mode_list.append(data_table[i][0])
                
            elif data_table[i][1] == lrg:
                mode_list.append(data_table[i][0])
        #converting list of modes into a string
        mode_string_temp = str(mode_list).strip("[")
        mode_string = mode_string_temp.strip("]")
        
        print ("The Mode(s)=", mode_string)
        
        #median
        median_list = l_obs
        median_len = len(median_list) 
        #if there are odd no. of observations
        if median_len % 2 == 1:
            median_pos = median_len // 2
            median = median_list[median_pos]
            print ("The Median=", median)
        #if there are even no. of observations
        else:
            med_1 = median_len // 2
            med_2 = med_1 + 1
            median = (median_list[med_1] + median_list[med_2]) / 2
            print ("Median=", median)

#grouped data
elif data == 2:
    total = 0
    print("You have selected Grouped data:")
    # minimum size can be 1
    while condition ==0:
        size = int(input("Please enter the class size:"))
        if size > 0:
            condition =1
        else:
            print ("please enter a valid class size")   
    #the range of upper lim. and lower lim. should be divisible by the size to make equal, continuous classes
    low_lim = int(input("Please enter the lower limit of the data:"))
    while condition == 1:
        up_lim = int(input("Please enter the upper limit of the data:"))
        range_dat = up_lim - low_lim
        if up_lim < low_lim:
            print ("Please enter a valid Upper limit")
            condition = 1
        if range_dat % size == 0:
            condition = 0
        else:
            print ("Please enter a valid Upper limit")
    
    class_list = []
    data_table = []
    #appending lower limit, upper limit and frequency into a list adn the appending that list into another list
    while low_lim < up_lim:
        class_list.append(low_lim)
        class_list.append(low_lim + size)
        print ("Enter the frequency for the class", low_lim, "-", low_lim + size, ":", end = "")
        freq = int(input())
        total = total + freq
        class_list.append(freq)
        data_table.append(class_list)
        class_list = []
        low_lim = low_lim + size

    print ("Your classes are([lower limit, upper limit, frequency]):")
    print (data_table)

    #if there is only one class
    if len(data_table) == 1:
        #mean
        xi = (data_table[0][0] + data_table[0][1]) / 2
        xifi = data_table[0][2] * xi
        mean = xifi / total
        print ("The Mean is=", mean)
        
        #mode
        mode = data_table[0][0] + (size / 2)
        print ("The Mode is=", mode)
        
        #median
        median = data_table[0][0] + ((data_table[0][2] ** 2) / 2) * size
        
        print ("The Median is=", median)

    else:
        #mean 
        #using formula (sig.xifi/n)
        xi_list = []
        xi = (data_table[0][1] - data_table[0][0]) / 2
        xi_list.append(xi)
        
        for i in range(0, len(data_table) - 1):
            xi = xi + size
            xi_list.append(xi)
        xifi_list = []  
        
        sum_freq = 0
        total_obs = 0
        for j in range(0, len(xi_list)):
            xifi = xi_list[j] * data_table[j][2]
            total_obs = total_obs + data_table[j][2]
            sum_freq = sum_freq + xifi
        
        mean = sum_freq / total_obs
        print ("The mean is=", mean)
        
        #mode 
        #using formula [l + ((f0 - fp)/(2f0 - fp - fs)) * h]
        #there can be multiple modes
        modpos_list = []
        for i in range(0, len(data_table)):
            if i == 0:
                lrg = data_table[i][2]
            
            if data_table[i][2] > lrg:
                modpos_list = []
                lrg = data_table[i][2]
                mode_pos = i
                modpos_list.append(mode_pos)
                
            elif data_table[i][2] == lrg:
                mode_pos = i
                modpos_list.append(mode_pos)      
        
        mode_list = []    
        for j in range(0, len(modpos_list)):
            
            if modpos_list[j] == 0:
                mod_l_lim = data_table[modpos_list[j]][0]
                f0 = data_table[modpos_list[j]][2]
                fp = 0
                fs = data_table[1][2]
                mode = mod_l_lim + ((f0 - fp)/(2*f0 - fp - fs)) * size
                mode_list.append(mode)
                
            elif modpos_list[j] == len(data_table) - 1:
                mod_l_lim = data_table[modpos_list[j]][0]
                f0 = data_table[modpos_list[j]][2]
                fp = data_table[modpos_list[j]-1][2]
                fs = 0
                mode = mod_l_lim + ((f0 - fp)/(2*f0 - fp - fs)) * size
                mode_list.append(mode)
                
            else:
                mod_l_lim = data_table[modpos_list[j]][0]
                f0 = data_table[modpos_list[j]][2]
                fp = data_table[modpos_list[j]-1][2]
                fs = data_table[modpos_list[j]+1][2]
                mode = mod_l_lim + ((f0 - fp)/(2*f0 - fp - fs)) * size
                mode_list.append(mode)
            
        mode_string_temp = str(mode_list).strip("[")
        mode_string = mode_string_temp.strip("]")
        
        print ("The Mode(s)=", mode_string)
        
        #median
        #using formula [l + (((n/2) - cf) / f) * h]
        half = total / 2
        cf = 0
        i = 0
        while cf <= half:
            cf = cf + data_table[i][2]
            i = i + 1
        median_pos = i - 1
        med_l_lim = data_table[median_pos][0]
        freq = data_table[median_pos][2]
        prev_cf = 0
        if median_pos == 0:
            prev_cf = 0
        else:
            for i in range(0, median_pos):
                prev_cf = prev_cf + data_table[i][2]
        
        median = med_l_lim + ((half - prev_cf) / (freq)) * size
        
        print ("The Median=", median)        