import socket

ip   = "127.0.0.1"
port = 5678

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.connect((ip,port))


print(f"Соединение с {ip} установлено...")
file = open('Transfer.txt', 'rb')
s.sendfile(file)
file.close()
print("Файл передан!")