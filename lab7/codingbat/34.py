def count_hi(str):

    for i in range (len(str)):
        if str[i] == 'h' and str[i+1] == 'i':
            counter+=1
    return counter
