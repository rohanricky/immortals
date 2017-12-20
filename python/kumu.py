import sys
import socket
#Implement WebSockets for faster communication
# use gRPCs if the files get complex and microservices are a must

def main(data,ip,port):
    link=data.split()
    if data.startswith('remote'):
        data=data.split(' ',1)[1]
        x=Socket(2048,ip,port)
        x.connect()
        x.sendtoserver(data)
#        print(link[1:])
    else:print(data)

class Socket:
    def __init__(self,message_length,ip,port,sock=None):
        if sock is None:
            self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        else:
            self.sock=sock
        self.message_length=message_length
        self.ip=ip
        self.port=port

    def connect(self):
        self.sock.connect(('192.168.43.167',5454))

    def sendtoserver(self,msg):
        total_sent=0
        self.sock.settimeout(3.0)
        print("Task Accomplished")
        while total_sent < self.message_length:
            sent=self.sock.send(msg[total_sent:])
            if sent==0:
                break
            total_sent+=sent
        self.sock.close()

if __name__=='__main__':
    data=sys.argv[1]
    ip=sys.argv[2]
    port=sys.argv[3]
    main(data.lower(),ip,port)
