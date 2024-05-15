import socket

class TCPClient:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))

    def send_command(self, command):
        self.client_socket.sendall(command.encode())
        response = self.client_socket.recv(1024)
        return response.decode()

    def close(self):
        self.client_socket.close()

if __name__ == "__main__":
    client = TCPClient()
    print(client.send_command("HELLO"))
    print(client.send_command("TIME"))
    print(client.send_command("UNKNOWN"))
    client.close()
