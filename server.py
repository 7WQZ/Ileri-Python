import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = socket.gethostname()
print("Bilgisayar adı: ", HOST)

HOST_IP = socket.gethostbyname(socket.gethostname())
print("server socket IP:  ", HOST_IP)

port = 12345

server_socket.bind((HOST_IP, port))
server_socket.listen()

while True:
    client_socket, client_adres = server_socket.accept()
    print("servera bağlanan client adresi: ", client_adres)
    print("servera bağlanan client socket: ", client_socket)

    client_socket.send(b"Merhaba Client".encode("UTF-8"))
    server_socket.close()
    break
