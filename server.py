import socket
from encoder import encode, decode
from middleware import headerMiddlewareFactory, loggingMiddlewareFactory
from router import router

PORT = 8000
HOST = "127.0.0.1"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Listening on port {PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            if not data:
                continue
            request = decode(data)
            middlewareChain = loggingMiddlewareFactory(router)
            middlewareChain = headerMiddlewareFactory(middlewareChain)
            responseBytes = encode(middlewareChain(req=request))
            conn.sendall(responseBytes)