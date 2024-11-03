import socket
import threading

class Broker:
    def __init__(self):
        self.workers = ['localhost:5001', 'localhost:5002', 'localhost:5003']
        self.request_count = [0, 0, 0]  # Untuk load balancing
        self.current_worker = 0

    def distribute_request(self, request):
        # Pendekatan 1: Pemerataan
        worker_index = self.request_count.index(min(self.request_count))
        self.request_count[worker_index] += 1
        
        # Pendekatan 2: Berurutan
        # worker_index = self.current_worker
        # self.current_worker = (self.current_worker + 1) % len(self.workers)

        worker_address = self.workers[worker_index]
        print(f"[Broker] Forwarding request to {worker_address} with request: {request}")
        
        worker_host, worker_port = worker_address.split(':')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((worker_host, int(worker_port)))
            sock.send(request.encode())
            response = sock.recv(1024).decode()
            print(f"[Broker] Received response: {response}")

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', 5000))
        server.listen(5)
        print("[Broker] Listening on port 5000")

        while True:
            client_socket, addr = server.accept()
            print(f"[Broker] Accepted connection from {addr}")
            request = client_socket.recv(1024).decode()
            self.distribute_request(request)
            client_socket.close()

if __name__ == "__main__":
    broker = Broker()
    broker.start()