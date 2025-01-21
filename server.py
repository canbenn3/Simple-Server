import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 8000))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Someone connected to your server! {conn}, {addr}")
            data = conn.recv(1024)
            if not data:
                continue
            print("Message received: ", data.decode())
            response = "Please send me data to steal >:D"
            conn.sendall(response.encode())