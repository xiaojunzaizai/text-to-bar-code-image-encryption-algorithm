import socket
import encryption_decryption

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 6666
s.connect((host,port))
m1= s.recv(1024).decode()
print(m1)
while True:
    m2 = input('Message:  ')
    en_m2 = encryption_decryption.encrytpion(m2)
    en_m2_len = str(len(en_m2))
    s.send(en_m2_len.encode())
    print('Size of the Data: ',end='')
    print(en_m2_len)
    s.send(en_m2)
    print(s.recv(1024).decode())
    if m2 == 'exit':
        print(s.recv(1024).decode())
        break

s.close()