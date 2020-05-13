import socket
import encryption_decryption

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 6666
s.bind((host,port))
s.listen(5)
while True:
    client, addr = s.accept()
    print('Accept new connection from %s:%s' % addr)
    client.send(b'Connect to the Server\nWelcome!!!\nPlease,enter your message\n')
    while True:
        en_data_size = client.recv(1024).decode()
        received_size = 0
        en_data = b''
        print('Size of the Data: ',end='')
        print(en_data_size)
        while received_size < int(en_data_size):
            received_data = client.recv(1024)
            received_size +=len(received_data)
            en_data += received_data
        de_data = encryption_decryption.decryption(en_data)
        message = 'Receive your message: ' + str(de_data)
        m2 = '\nMessage Received\n'
        print(message)
        client.send(m2.encode())
        if de_data == 'exit':
            client.send(b'Good bye! \n')
            break
    client.close()
    print("Connection from %s:%s is closed" % addr)
    break








