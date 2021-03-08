

class redundantBit:  # class redundantBit
    def __init__(self, number):
        self.number = number  # position number
        self.bit = None  # position bit content
        # redundantBit components linked with original bit for exaple position 1(2^0) = {3, 5, 7}
        self.link = []


class originalBit:
    def __init__(self, b, number):
        self.number = number    # bit number
        self.bit = int(b)  # bit content
        # bit linked with postion(redundantBit) for example 7 = 1(2^0) + 2(2^1) + 4(2^2), 6 = 2 + 4, 5 = 1 + 4.......
        self.link = []


def redundantNumber(m):  # m+r+1 < 2^r: k+r+1 < 2^r
    r = 1
    while m > 2**r-r-1 :
        r = r + 1        # increase r
    return r             # return r


def generateHamingListAndReduntantList(codeword):
    hammingCode = []        # list stores hamming code
    hammingCode.append(0)   # start with 1 instead of 0
    postionList = []          # redundant list
    for i in range(1, len(codeword) + 1):  # From index 1 to last
        # locals() return a dictionary with key 'bi' and update bit number and bit content in codeword
        locals()['b' + str(i)] = originalBit(int(codeword[i - 1]), i)
        # Update hammingCode with dictionary
        hammingCode.append(locals()['b' + str(i)])
             
    r = redundantNumber(len(codeword))  # get rendundant numbers
    for j in range(1, r + 1):
        locals()['P' + str(j)] = redundantBit(j)  # same with last for-loop
        # as 2^(j-1) or 2^r index to insert postion bits into hammingCode
        hammingCode.insert(2 ** (j - 1), locals()['P' + str(j)])
        postionList.append(2 ** (j - 1))  # unpate postionList with postion number

            
    
    #Now we need to find out the postions related with each bit number
    for i in range(1, len(hammingCode)):
        bitNo = 0

        if i in postionList: #if index is a position, skip 
            continue

        bitNo = i  # record bit number
        for j in range(len(postionList) - 1, -1, -1): #from range 
            if bitNo >= postionList[j]:
                bitNo = bitNo - postionList[j]
                hammingCode[i].link.append(postionList[j])  
            if bitNo == 0:
                break
        
        for k in hammingCode[i].link:
            hammingCode[k].link.append(i)
    
    print(hammingCode[1].link)
    print(hammingCode[2].link)
    print(hammingCode[4].link)

   



codeword = '1011'
generateHamingListAndReduntantList(codeword)


   

