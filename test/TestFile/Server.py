# tcp服务端发送接受消息
import socket
def Server_Test():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("开始建立服务器连接..........")
    ip_prot = ('127.0.0.1', 9999)
    s.bind(ip_prot) #监听该地址
    s.listen(5)
    con,adder = s.accept()
    print('Accept new connection from %s:%s...' % con)
    print(s.recv(1024).decode())
    print('Connection from %s:%s closed.' % adder)
    data = "hello,word".encode()
    s.send(data)
    s.close()
Server_Test()