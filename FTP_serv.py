import socket

ip   = "127.0.0.1"
port = 5678

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((ip, port))
s.listen(1)
conn, rem_ip = s.accept()
print(f"Соединение с {rem_ip} установлено!")

data = conn.recv(4096)
print(data)

file = open("Transfered.txt", "a")
file.write(data.decode())
file.close()
print("Файл передан!")