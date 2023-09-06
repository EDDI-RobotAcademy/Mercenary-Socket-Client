import socket
import logging
import sys

import multiprocessing as mp
import time

from receiver.rx import Receiver


class SocketClient:
    def __init__(self):
        # AWS Elastic IP 입력(추후 secrets 등 외부 변수 주입 방법 필요)
        self.server_address = "localhost"

        self.receiver = Receiver()
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def run(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
                server_socket.connect((self.server_address, 33333))
                server_socket.setblocking(False)
                receiver_process = mp.Process(target=self.receiver.receive_command,
                                              args=(server_socket,))
                receiver_process.daemon = True
                receiver_process.start()

                while True:
                    time.sleep(0.5)
                    # msg = input('Enter command: ')
                    # if len(msg.strip()) > 0:
                    #     self.logger.info('send [{}] command to server'.format(msg))
                    #     sd.sendall(msg.encode())
                    #     response = sd.recv(1024)
                    #     self.logger.info(response.decode())
                    # else:
                    #     self.logger.info('enter the command!!!')
                    #     sys.exit(1)

        except Exception as e:
            self.logger.info(e)


if __name__ == '__main__':
    app = SocketClient()
    app.run()
