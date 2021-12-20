transformation={
    'A':0,
    'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,
    'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25
}

def encrypter(string,n):
    temp_string=string.upper()
    # print(temp_string)
    string2=[]
    for i in temp_string:
        c_index=transformation[i]
        to_index=(c_index+n)%26
        for i in transformation:
            if(transformation[i]==to_index):
                string2.append(i)
    # print(string2)
    encrypted=""
    for i in string2:
        encrypted=encrypted+i
    print('Encrypted Value = ',encrypted)

encrypter('DEFENDTHEFORT',7)

def decrypter(string,n):
    temp_string=string.upper()
    # print(temp_string)
    string2=[]
    for i in temp_string:
        c_index=transformation[i]
        to_index=((c_index-n))%26
        for i in transformation:
            if(transformation[i]==to_index):
                string2.append(i)
                break
    # print(string2)
    encrypted=""
    for i in string2:
        encrypted=encrypted+i
    print('Decrypted Value = ',encrypted)

decrypter('KLMLUKAOLMVYA',7)

print('Hello guyz!!!')