def encodeString(stringVal):
    prevChar = stringVal[0]
    count = 0
    encodedList=[]
    for char in stringVal:
        if prevChar != char :
            encodedList.append((prevChar,count))
            count =0
        prevChar = char
        count= count+1
    
    encodedList.append((prevChar,count))
    return encodedList

def decodeString(encodedList):
    decodedStr = ''
    for key,value in encodedList:
        decodedStr= decodedStr + key * value
    return decodedStr

print(encodeString("Bookkeeping"))
print(decodeString([('W',5),('e',2),('t',5)]))
