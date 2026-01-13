import socket

CLIENT = socket.gethostbyname(socket.gethostname())
PORT = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((CLIENT, PORT))

while True:
    message = client_socket.recv(1024).decode("UTF-8")

    if message == "quit":
        client_socket.send("quit".encode("UTF-8"))
        print("Çıkış yapılıyor...")
        break
    else:
        print(f"{message}\n")
        message = input("yeni mesajını giriniz: ")

        client_socket.send(message.encode("UTF-8"))
        
client_socket.close()        