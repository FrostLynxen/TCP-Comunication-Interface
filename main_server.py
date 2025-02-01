# echo_server.py
import socket

HOST = ''  # or '' to accept connections on all interfaces
PORT = 8500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server listening on {HOST}:{PORT}")
    conn, addr = server.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Received:", data.decode())
            conn.sendall(data)  # echo back the received data