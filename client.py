import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = socket.gethostname()

HOST_IP = socket.gethostbyname(HOST)

port = 12345

client_socket.connect((HOST_IP, port))
message = client_socket.recv(1024)
print("Gelen mesaj: ", message.decode("UTF-8"))
client_socket.close()
