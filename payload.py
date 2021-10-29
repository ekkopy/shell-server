import socket
import subprocess

credentials = ["root:123456", "root:toor", "admin:123456"]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 333)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(server_address)
sock.listen(5)

while True:
    connection , client_address = sock.accept()
    print(f"[*] New connection from {client_address}")
    try:
        connection.send(b"[*] Username: ")
        username = connection.recv(32).strip().decode('utf-8')
        connection.send(b"[*] Password: ")
        password = connection.recv(32).strip().decode('utf-8')
        if "{0}:{1}".format(username, password) in credentials:
            connection.send(b"\nWelcome to socket server panel. \n")

            while True:
                connection.send(b"$ ")
                data = connection.recv(1024).strip().decode('utf-8')
                if data == "exit":
                    break
                if data == "shell":
                    while True:
                        connection.send(b"shell >>: ")
                        datapoint = connection.recv(2048)
                        proc = subprocess.Popen(datapoint, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        stdout_value = b'\n' + proc.stdout.read() + proc.stderr.read() + b'\n'
                        connection.send(stdout_value)

                if data == "server info":
                    cmdserver = "uname -a"
                    proc = subprocess.Popen(cmdserver, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    stdout_value = b'\n' + proc.stdout.read() + proc.stderr.read() + b'\n'
                    connection.send(stdout_value)

                else:
                    connection.send(b"Command not found: " + data + b'\n')

        else:
            connection.send(b"Access denied.")

    except socket.error:
        print("An error occured with client ip={0}, port{1}".format(*client_address))

    finally:
        connection.close()
