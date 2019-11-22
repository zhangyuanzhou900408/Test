# tcp客服端发送消息
import socket
def Client_Test():
    #发送数据
    connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip_prot=('127.0.0.1', 9999)
    connect.connect(ip_prot)
    print("服务器连接中.......")
    connect.send("恭喜你收到服务器数据".encode())
    #接受数据
    buffer = []
    while True:
        d= connect.recv(1024).decode()
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    print("数据接受中............")
    print(data)
    connect.close()
Client_Test()