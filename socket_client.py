import socket
import logging
import sys

import multiprocessing as mp
import time

from config.socket_config import SocketConfig
from receiver.rx import Receiver
from task_manager.manager import Manager


class SocketClient:
    def __init__(self):
        print("SocketClient Constructor")
        self.socket_config = SocketConfig()
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.manager = Manager()

    def run(self):
        try:
            print("SocketClient run()")

            self.socket_config.connect()
            print("After connect()")
            #print("socket fd: ", self.socket_config.get_server_socket())

            server_socket = self.socket_config.get_server_socket()

            self.socket_config.turn_on_non_blocking()
            self.manager.start_all_threads(server_socket)
            # receiver_process = mp.Process(target=self.receiver.receive_command,
            #                               args=(server_socket,))
            # receiver_process.daemon = True
            # receiver_process.start()

            while True:
                time.sleep(1)
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
