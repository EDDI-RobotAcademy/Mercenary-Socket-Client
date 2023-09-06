import socket
from decouple import config


class SocketConfig:
    def __init__(self):
        self.host = config('HOST')
        self.port = int(config('PORT'))
        self.client_socket = None

    def set_host(self, host):
        self.host = host

    def set_port(self, port):
        self.port = port

    def create_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        if not self.client_socket:
            self.create_socket()

        try:
            self.client_socket.connect((self.host, self.port))
            print(f"Connected to {self.host}:{self.port}")
        except ConnectionRefusedError:
            print(f"Connection to {self.host}:{self.port} refused.")
        except Exception as e:
            print(f"Error while connecting: {str(e)}")

    def close(self):
        if self.client_socket:
            self.client_socket.close()
            print("Socket closed.")
            self.client_socket = None


# 사용 예시
if __name__ == "__main__":
    config = SocketConfig()
    config.connect()
    config.close()
