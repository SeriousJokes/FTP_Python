import ftplib
import os

host = input('Введите FTP сервер к которому хотите подключиться!\n')
user = input('Введите имя пользователя!\n')
password = input('Введите пароль!\n')

ftp = ftplib.FTP(host)
output = ftp.login(user, password)

if '230' in output:
    print('Подключение к серверу установлено!')

print(ftp.pwd())

while True:
    cmd = input()
    if 'cd' or 'cwd' in cmd:
        space = cmd.find(' ')
        ftp.cwd(cmd[space+1:])
        print(ftp.pwd())
    if cmd == 'pwd':
        print(ftp.pwd())
    if cmd == 'dir' or cmd == 'ls':
        print(ftp.dir())
    if cmd == 'exit' or cmd == 'close':
        ftp.close()
        print('Соединение с сервером закрыто!')