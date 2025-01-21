import socket

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        data = input("Enter your information :]")
        if data == "exit":
            break
        s.connect(("127.0.0.1", 8000))
        s.sendall(data.encode())
        response = s.recv(1024)
        print("response recieved:", response)