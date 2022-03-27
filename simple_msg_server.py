import socket

def send(idata):
    idata = idata.encode()
    client.send(idata)
    print("waiting for msg\n")
    
def recive():
    odata = client.recv(1024)
    odata=odata.decode()
    return odata

HOST = '127.0.0.1'
PORT = 8081 
server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)
client, client_addr = server.accept()
print('[+] Server Started')
print('[+] Listening For Client Connection ...')
print(f'[+] {client_addr} Client connected to the server')

while True:
    instruction = input(">>\t")
    send(instruction)
    instruction = recive()
    print(instruction)