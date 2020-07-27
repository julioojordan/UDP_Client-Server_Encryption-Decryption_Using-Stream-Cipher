#UDP Python with stream chiper encryption
#by Julio Andyan Jordan Aryanto
#nim 24060117130078
#client

from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
#clientSocket.connect((serverName, serverPort))
message = input('Masukan plainteks:')
U = input('Masukan nilai U (min 4 bit): ')


#mengubah pesan ke binary
#binMessage = ''.join(format(ord(i), 'b') for i in message)
binary_int = int.from_bytes(message.encode(), "big")
binMessage = bin(binary_int).replace("0b", "")

#mengirimkan pesan ke server
clientSocket.sendto(message.encode(),(serverName, serverPort))
clientSocket.sendto(U.encode(),(serverName, serverPort))


#mengambil pesan dari server
binary_string, serverAddress =clientSocket.recvfrom(2048)
k, serverAddress =clientSocket.recvfrom(2048)


#menampilkan pesan
print (binary_string.decode())
print (k.decode())
clientSocket.close()
