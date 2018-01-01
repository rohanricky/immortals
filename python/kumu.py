import sys
import socket
#Implement WebSockets for faster communication
# use gRPCs if the files get complex and microservices are a must
class Socket:
    def __init__(self,message_length,sock=None):
        if sock is None:
            self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        else:
            self.sock=sock
        self.message_length=message_length

    def connect(self):
        self.sock.connect(('192.168.43.167',7823))

    def sendtoserver(self,msg):
        total_sent=0
        self.sock.settimeout(3.0)
        while total_sent < self.message_length:
            sent=self.sock.send(msg[total_sent:])
            if sent==0:
                break
            total_sent+=sent
        self.sock.close()
        return "Task Accomplished"

    def receive(self):
        chunks=[]
        bytes_recv=0
        while bytes_recv<self.message_length:
            chunk=self.sock.recv(min(self.message_length-bytes_recv,2048))
            if chunk==b'':
                break
            chunks.append(chunk)
            bytes_recv+=len(chunk)
        print(b''.join(chunks))

def main(data):
    link=data.split()
    if data.startswith('remote'):
        data=data.split(' ',1)[1]
        x=Socket(2048)
        x.connect()
        y=x.sendtoserver(data.encode())
        return y
    else:return data

if __name__=='__main__':
    data=sys.argv[1]
    main(data.lower())
