import socket
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

host = "localhost"
port = 8081
filename = "data.txt"

# 获取文件大小
filesize = os.path.getsize(filename)

s = socket.socket()
print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

# 开始发送文件
with open(filename, "rb") as f:
    while True:
        # 从文件读取字节流
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # 没有数据时结束
            break

        s.sendall(bytes_read)

# 关闭socket
s.close()
