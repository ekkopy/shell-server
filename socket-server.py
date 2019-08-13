import socket
import subprocess

# cred
cred = ["root:toor"]
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 333)
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sck.bind(server_addr)
sck.listen(5)


while True:
    connection, client_addr = sck.accept()
    print("[*] New connection: {0}:{1}".format(*client_addr))
    #print(f"[*] New connection from: {client_addr}")
    try:
        connection.send(b"Username: ")
        username = connection.recv(32).strip().decode('utf-8')
        connection.send(b"Password: ")
        password = connection.recv(32).strip().decode('utf-8')
        if "{0}:{1}".format(username, password) in cred:
            connection.send(b"\nWelcome to socket server panel!")
            while True:
                connection.send(b"$ ")
                data = connection.recv(1024).strip().decode('utf-8')
                if data == "exit":
                    break
                elif data == "shell":
                    while True:
                        connection.send(b"root@universe: ")
                        datapoint = connection.recv(2048)
                        proc = subprocess.Popen(datapoint, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
                        stdout_value = b'\n' + proc.stdout.read() + proc.stderr.read() + b'\n'
                        connection.send(stdout_value)
                elif data == "server_info":
                    cmdserver = "uname -a"
                    proc = subprocess.Popen(cmdserver, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    stdout_value = b'\n' + proc.stdout.read() + proc.stderr.read() + b'\n'
                    connection.send(stdout_value)
                else:
                    connection.send(b"Command not found: " + data + b'\n')
        else:
            connection.send(b"Access Denied!!")
    except socket.error as sck_error:
        print(f"Error reported: {client_addr}")
    finally:
        connection.close()

