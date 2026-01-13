import socket

SERVER = socket.gethostbyname(socket.gethostname())

PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER, PORT))
server_socket.listen()
print("server çalışıyor...")

client_socket,client_adres= server_socket.accept()
client_socket.send("servera bağlantınız sağlandı".encode("UTF-8"))

while True:
    message = client_socket.recv(1024).decode("UTF-8")
    if message=="quit":
        client_socket.send("quit".encode("UTF-8"))
        print("Çıkış yapıldı...")
        break
    else: 
        print(f"{message}\n")
        message = input("yeni mesajı giriniz: ")
        client_socket.send(message.encode("UTF-8"))

server_socket.close()