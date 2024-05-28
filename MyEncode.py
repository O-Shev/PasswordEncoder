#encoder
#keyword for email: blablabla@gmail.com.MY_SOLD.2024
#where 2024 - year of creating password
#keyword for services:  blablabla@gmail.com.MY_SOLD.2024.cloudflare
#KeyPin is sequence of numbers in rage {2;7}


from hashlib import sha256

esc = ''
while(esc!='.q'):
    hasError = True
    while(hasError):
        strKeyWord=input("KeyWord:")
        strKeyPin =input("KeyPin:")
        if(strKeyWord == '' or strKeyPin == ''): print("KeyWord and KeyPin should not be empty")
        elif(not strKeyPin.isdigit()): print("KeyPin should contain only digits")
        else: hasError = False

    encodedKeyWord = list(sha256(strKeyWord.encode('utf-8')).hexdigest())
    arrKeyPin = list(strKeyPin)

    encodedResultArray = []

    iteratorAcrossPin = 0
    while(encodedKeyWord):
        popChar1 = encodedKeyWord.pop(0)
        resChar = ''
        if(0x2<=int(popChar1, 16)<=0x7):
            if(encodedKeyWord): resChar = popChar1 + encodedKeyWord.pop(0)
            else: 
                resChar = arrKeyPin[iteratorAcrossPin] + popChar1
        else: 
            resChar = arrKeyPin[iteratorAcrossPin] + popChar1
            if(iteratorAcrossPin<len(arrKeyPin)-1): iteratorAcrossPin+=1
            else: iteratorAcrossPin = 0
        if(resChar != '7f' and resChar != '7F'): encodedResultArray.append(resChar)
        else: 
            if(encodedResultArray): encodedResultArray.pop()
    

    encodedResultString = ''
    for i in encodedResultArray:
        encodedResultString +=bytes.fromhex(i).decode("utf-8")
    
    while(encodedResultString[-1]==' '):
        encodedResultString=encodedResultString[:-1]
    print('--------------------Result Password--------------------')
    print(encodedResultString)
    print('-------------------------------------------------------')

    esc = input()
    iteratorAcrossPin = 0    

