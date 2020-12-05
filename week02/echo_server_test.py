#!/usr/bin/env python
# 服务端
import socket

HOST = "localhost"
PORT = 8889

def echo_server():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 对象s绑定到指定的主机和端口上
    s.bind((HOST, PORT))
    # 只接受1个连接
    s.listen(1)

    while True:
        # accept 表示接受用户端的连接
        conn, addr = s.accept()
        # 输出客户端地址
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data)
            conn.sendall(data)
        conn.close()
        
    s.close()

if __name__ == '__main__':
    echo_server()
