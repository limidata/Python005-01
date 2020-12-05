import socket
import os

SERVER_HOST = "localhost"
SERVER_PORT = 8081

BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))

s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

client_socket, address = s.accept()
print(f"[+] {address} is connected.")

# 接收文件信息
received = client_socket.recv(BUFFER_SIZE).decode()
print(received)

filename, filesize = received.split(SEPARATOR)
# 得到文件名
filename = os.path.basename(filename)

# 读取内容写入文件
with open(filename + ".log", "wb") as f:
    while True:
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        f.write(bytes_read)


client_socket.close()

s.close()
