def moveZero(my_num):
    try:
        #check if its num
        int(my_num)
        res = str(my_num)
        quitZ = res.replace('0','')
        toEnd = quitZ.ljust(len(res), '0')
        return int(toEnd)    
    except :
        print ('Non numeric data found.')

