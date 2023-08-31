import socket
import logging
import sys


class SocketClient:
    def __init__(self):
        # AWS Elastic IP 입력(추후 secrets 등 외부 변수 주입 방법 필요)
        self.server_address = "localhost"
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def run(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sd:
                sd.connect((self.server_address, 33333))
                msg = input('Enter command: ')
                if len(msg.strip()) > 0:
                    self.logger.info('send [{}] command to server'.format(msg))
                    sd.sendall(msg.encode())
                    response = sd.recv(1024)
                else:
                    self.logger.info('enter the command!!!')
                    sys.exit(1)

            self.logger.info(response.decode())
        except Exception as e:
            self.logger.info(e)


if __name__ == '__main__':
    app = SocketClient()
    app.run()
