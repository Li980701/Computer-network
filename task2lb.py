def redundantNumber(m):  # m+r+1 < 2^r: k+r+1 < 2^r
    r = 1
    while m > 2**r-r-1 :
        r = r + 1        # increase r
    return r  # return r
    
#implement (11,7) hamming code
ck1 = [3, 5, 7, 9, 11]
ck2 = [3, 6, 7, 10, 11]
ck3 = [5, 6, 7]
ck4 = [9, 10, 11]

def hamming_code_generator(codeword):
    count = 0                               
    redunNumber = redundantNumber(len(codeword))  #check hom many redundant number that requires 
    hammingList = list(range(redunNumber+len(codeword)))  #define hamming list length 
    hammingList.append(0)
    codewordList = list(codeword)
    ckbit1 = 0
    ckbit2 = 0
    ckbit3 = 0
    ckbit4 = 0
    #since I just simply implement 11,7 hamming code so define index 1 2 4 8 as postion bits
    for i in range(1, len(hammingList)):
        if i == 1 or i ==2 or i==4 or i==8:   #postion bits
            hammingList[i] = None
            continue                            #skip postion bits 
    
        hammingList[i] = codewordList[count]
        count = count + 1
    
    hammingList[0] = 'skip'                 #ignore the first bit
    # print(hammingList)
        
    # 3 = 1+2        ck1 = [3,5,7,9,11]
    # 5 = 1+4        ck2 = [3,6,7,10,11]
    # 6 = 2+4        ck3 = [5,6,7]
    # 7 = 1+2+4      ck4 = [9,10,11]
    # 9 = 1+8
    # 10 = 2+8
    # 11 = 1+2+8
   
    
    for i in range(0,len(ck1)): #sum ck1, ck2, ck3, ck4 to do parity
        ckbit1 = ckbit1 + int(hammingList[ck1[i]])

    for i in range(0,len(ck2)):
        ckbit2 = ckbit2 + int(hammingList[ck2[i]])

    for i in range(0,len(ck3)):
        ckbit3 = ckbit3 + int(hammingList[ck3[i]])

    for i in range(0,len(ck4)):
        ckbit4 = ckbit4 + int(hammingList[ck4[i]])

    for i in range(1, len(hammingList)):  #Parity and Replace
        if i == 1:
            if(ckbit1%2==0):
                hammingList[i] = '0'
            else:
                hammingList[i] = '1'
        if i == 2:
            if(ckbit2%2==0):
                hammingList[i] = '0'
            else:
                hammingList[i] = '1'
        if i == 4:
            if(ckbit3%2==0):
                hammingList[i] = '0'
            else:
                hammingList[i] = '1'
        if i == 8:
            if(ckbit4%2==0):
                hammingList[i] = '0'
            else:
                hammingList[i] = '1'

    hammingList.pop(0)  #remove skip
    hammingCode = "".join(hammingList)
    print('THE HAMMING CODE IS :', hammingCode)
    return hammingCode

def hamming_code_error_detection(received_data):
    receivedList = list(received_data)
    print("reveivedList is :", receivedList)
    ckbit1 = 0
    ckbit2 = 0
    ckbit3 = 0
    ckbit4 = 0
    for i in range(0,len(ck1)):
        ckbit1 = ckbit1 + int(receivedList[ck1[i] - 1])
    for i in range(0,len(ck2)):
        ckbit2 = ckbit2 + int(receivedList[ck2[i]-1])
    for i in range(0,len(ck3)):
        ckbit3 = ckbit3 + int(receivedList[ck3[i]-1])
    
    for i in range(0,len(ck4)):
        ckbit4 = ckbit4 + int(receivedList[ck4[i]-1])
    if ckbit1 % 2 == 0:
        ckbit1 = 0
    else:
        ckbit1 = 1
    if ckbit2 % 2 == 0:
        ckbit2 = 0
    else:
        ckbit2 = 1
    if ckbit3 % 2 == 0:
        ckbit3 = 0
    else:
        ckbit3 = 1
    if ckbit4 % 2 == 0:
        ckbit4 = 0
    else:   
        ckbit4 = 1
    countErrorBit = 0
    cklist = [ckbit1, ckbit2, ckbit3, ckbit4]
    for i in range(0, 4):
        if int(receivedList[2 ** i - 1]) == cklist[i]:
            continue
        else:
            countErrorBit += 2**i
    
    print(ckbit1)
    print(ckbit2)
    print(ckbit3)
    print(ckbit4)
    print("------")
    print(cklist)
    print('------')
    print(countErrorBit)

    

received_data = '11111000011'
codeword = '1100011'
hamming_code_generator(codeword)
hamming_code_error_detection(received_data)
