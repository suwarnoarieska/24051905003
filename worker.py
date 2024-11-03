import socket
import threading
import time

def handle_client(client_socket):
    request = client_socket.recv(1024).decode()
    print(f"[Worker] Received request: {request}")
    
    # Simulasi aplikasi Long dan Short
    if request.startswith("Long"):
        time.sleep(5)  # Simulasi perhitungan kompleks
        response = "Long computation done"
    elif request.startswith("Short"):
        response = "Echo: " + request
    else:
        response = "Unknown request"
    
    client_socket.send(response.encode())
    client_socket.close()

def start_worker(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', port))
    server.listen(5)
    print(f"[Worker] Listening on port {port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[Worker] Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_worker(5001)  # Worker 1
    start_worker(5002)  # Worker 2
    start_worker(5003)  # Worker 3