import socket

def send_request(application_id):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(('localhost', 5000))
        sock.send(application_id.encode())
        response = sock.recv(1024).decode()
        print(f"[Client] Received response: {response}")

if __name__ == "__main__":
    while True:
        app_id = input("Enter application ID (Long/Short): ")
        send_request(app_id)