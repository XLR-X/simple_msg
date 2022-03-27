import socket

def send(idata):
    idata = idata.encode()
    client.send(idata)
    print("waiting for msg\n")
    
def recive():
    odata = client.recv(1024)
    odata=odata.decode()
    return odata

REMOTE_HOST = '127.0.0.1' 
REMOTE_PORT = 8081 
client = socket.socket()
client.connect((REMOTE_HOST, REMOTE_PORT))
print("[-] Connection Initiating...")
print("[-] Connection initiated!")


while True:
    instruction = recive()
    print(instruction)
    instruction = input(">>\t")
    send(instruction)