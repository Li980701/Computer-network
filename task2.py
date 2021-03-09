class redundantBit:  # class redundantBit
    def __init__(self, number):
        self.number = number  # position number
        self.bit = None  # position bit content
        # redundantBit components linked with original bit for exaple position 1(2^0) = {3, 5, 7}
        self.link = []

class originalBit:
    def __init__(self, b, number):
        self.bit = int(b)  # bit content
        self.number = number    # bit number
        # bit linked with postion(redundantBit) for example 7 = 1(2^0) + 2(2^1) + 4(2^2), 6 = 2 + 4, 5 = 1 + 4.......
        self.link = []

def redundantNumber(m):  # m+r+1 < 2^r: k+r+1 < 2^r
    r = 1
    while m > 2**r-r-1 :
        r = r + 1        # increase r
    return r             # return r

def generateHamingListAndReduntantList(codeword):
    hammingCode = []        # list stores hamming code
    hammingCode.append(0)  
    postionList = []          # redundant list
    for i in range(1, len(codeword) + 1):  # From index 1 to last
        hammingCode.append(originalBit(int(codeword[i - 1]), i)) 
    r = redundantNumber(len(codeword))  # get rendundant numbers
    for j in range(1, r + 1):
        hammingCode.insert(2 ** (j - 1), redundantBit(j)) # as 2^(j-1) or 2^r index to insert postion bits into hammingCode
        postionList.append(2 ** (j - 1))  # unpate postionList with postion number
    
    # print(postionList)       
    #Now we need to find out the postions related with each bit number
    for i in range(1, len(hammingCode)):
        bitNo = 0
        if i in postionList: #if index is a position, skip 
            continue

        bitNo = i  # record bit number
        for j in range(len(postionList) - 1, -1, -1): 
            if bitNo >= postionList[j]:
                bitNo = bitNo - postionList[j]
                hammingCode[i].link.append(postionList[j])  
            if bitNo == 0:
                break

    
        for k in hammingCode[i].link:
            hammingCode[k].link.append(i)
    
    #Now we can calculate hamming code 
    for j in postionList:
        xor = 0
        for i in hammingCode[j].link:
            xor = xor ^ hammingCode[i].bit
        hammingCode[j].bit = xor

        
    #print
    for i in range(1, len(hammingCode)):
        if i in postionList:  # 检测码
            print('\033[1;33m%d\033[0m' % hammingCode[i].bit, end='')
            print('\n')
        else:
            print('%d' % hammingCode[i].bit, end='')
            print('\n')
