import socket

class UDPClient:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_request(self, request):
        self.client_socket.sendto(request.encode(), (self.host, self.port))
        response, _ = self.client_socket.recvfrom(1024)
        return response.decode()

    def close(self):
        self.client_socket.close()

if __name__ == "__main__":
    client = UDPClient()
    print(client.send_request("USD"))
    print(client.send_request("EUR"))
    print(client.send_request("JPY"))
    print(client.send_request("BRL"))
    client.close()
