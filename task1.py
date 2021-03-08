def hamming_distance(codeword1, codeword2):
    if len(codeword1) != len(codeword2):
        print('two inputs value have different length')

    HDist = 0
    codewordone = list(codeword1)
    codewordtwo = list(codeword2)

    for i in range(len(codewordone)):
        if codewordone[i] != codewordtwo[i]:
            HDist = HDist + 1
    return HDist


def checking_codewords(codewords, received_data):
    # error message
    error = "error detected"
    # minHdist is the smallest Haiming distance in the input codewords
    minHdist = hamming_distance(codewords[0], codewords[1])
    for i in range(len(codewords)):
        for j in range(len(codewords)):
            if minHdist > hamming_distance(codewords[i], codewords[j]) and hamming_distance(codewords[i], codewords[j]) != 0:
                minHdist = hamming_distance(codewords[i], codewords[j])
    # Finish acquiring the smallest Haiming distance
    # Now we know the how many bits we can change for received data, must samller than or equal to the ((samllest Haiming distance)-1)/2
    bitsCorrect = int((minHdist - 1) / 2)
    received_data_before_changed = received_data
    for i in range(len(codewords)):
        # if recieved data can be corrected
        if len(codewords[i]) == len(received_data):
            if hamming_distance(codewords[i], received_data) <= bitsCorrect:
                received_data = codewords[i]
        else:  # if recieved data has deffernt length with codewords then break and return error
            print(error)
            return error

    if (received_data == received_data_before_changed):
        print(error)
        return error

    print('the data has been corrected:', received_data)


codewordes = ['0000000000', '0000011111', '1111100000', '1111111111', ]
received_data = '0100000000'
checking_codewords(codewordes, received_data)
