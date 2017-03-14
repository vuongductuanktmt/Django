# main program
for temp in range(30,300):#khoi tao temp tu 30 den 300
    if (temp%7==0 and temp%13==0): # neu temp chia het cho 7 va 13 thi in ra 'a-z'
        print 'a-z'
    elif (temp%7==0): # neu temp chi chia het cho 7 thi in ra 'xyz'
        print 'xyz'
    elif (temp%13==0):# neu temp chi chia het cho 13 thi in ra 'abc'
        print 'abc'
    else: # truong hop con lai in ra temp
        print temp
