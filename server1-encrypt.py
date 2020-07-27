#UDP Python with stream chiper encryption
#by Julio Andyan Jordan Aryanto
#nim 24060117130078
#server

from socket import *

#mengubah array menjadi integer
def array_int(array):
    array_int = []
    for i in range(len(array)):
        array_int.append(int(array[i]))
    return array_int

#mengubah array menjadi string
def array_str(array):
    array_str = []
    for i in range(len(array)):
        array_str.append(str(array[i]))
    return array_str


#list to string
def listToString(array):
    str1 = ''
    for i in range(len(array)):
        str1 += array[i]
    return str1

#mengubah biner ke decimal
def BinaryToDecimal(binary):  
         
    binary1 = binary  
    decimal, i, n = 0, 0, 0
    while(binary != 0):  
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)  
        binary = binary//10
        i += 1
    return (decimal)



serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('The server is ready to receive')
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    U, clientAddress = serverSocket.recvfrom(2048)

    #mengubah message menjadi str biner
    binMessage = ''.join(format(ord(i), 'b') for i in message.decode())

    #mengubah binMassage menjadi array integer
    binMessage = array_int(binMessage)

    #mengubah U menjadi array integer
    temp_keystream = U.decode()
    keystream = array_int(temp_keystream)
    
    #mengambil panjang pesan
    panjang_pesan = len(binMessage)

    
    #membuat keystream ide : meng XOR kan bit pertama dengan bit ke-4 dari U
    for i in range(3, panjang_pesan-1):
        add = keystream[i] ^ keystream[i-3]
        keystream.append(add)

    #melakukan proses enkripsi binMessage[i] XOR kestream [i]
    cipher = []
    for i in range(panjang_pesan):
        c = binMessage[i] ^ keystream[i]
        cipher.append(c)
        
    #mengubah list cihper int menjadi list str
    lstr_cipher = array_str(cipher)
    #list cipher str diubah ke dalam string dulu menggunakan
    #fungsi listTostring
    str_cipher = listToString(lstr_cipher)

    #mengubah ke dalam ASCII dan menyimpan ke cipherteks
    cipherteks = ''
    for i in range(0, len(str_cipher), 7): 
      
        # memotong array cipher ke index range [0, 6] 
        # dan menyimpannya ke temp_data 
        temp_data = int(str_cipher[i:i + 7]) 
       
        # memasukan temp_data kefungsi binarytoDecimal 
        decimal_data = BinaryToDecimal(temp_data) 
       
        # Deccoding nilai decimal hasil dari  
        # BinarytoDecimal() function, menggunakan chr()  
        # function yang akan menghasilkan string yang sesuai  
        # dengan karakter di tabel ASCII dan menyimpan ke
        # str_data 
        cipherteks = cipherteks + chr(decimal_data)

    
    print(message.decode())
    print(binMessage)
    print(keystream)
    print(cipher)
    print(cipherteks)
    m1 = binMessage
    
    binMessage.decode()
    print(binMessage)
    k = U
    print(U)
    k.decode()
    print(k)
    serverSocket.sendto(binMessage, clientAddress)
    serverSocket.sendto(k, clientAddress)
