import errno
import socket
import threading
import time

from datetime import datetime as dt


class Receiver:
    def __init__(self, receive_queue):
        print("Receiver Constructor")
        self.rx_thread = threading.Thread(target=self.receive_command,
                                          name='ReceiverThread')
        self.receiver_command_data_queue = receive_queue
        self.server_socket = None

    def start_rx_thread(self, server_socket):
        self.server_socket = server_socket
        self.rx_thread.start()

    def receive_command(self):
        print("start_rx_thread start!")
        while True:
            # with self.server_socket:
            print("wait for receive data")
            try:
                data = self.server_socket.recv(1024)
                response_str = data.decode().strip()
                print('{} command received [{}] from server'.format(dt.now(), response_str))

                split_data = data.decode().split(',')
                self.receiver_command_data_queue.put(split_data)

            except socket.error as e:
                if e.errno == errno.EWOULDBLOCK:
                    pass

            finally:
                time.sleep(0.5)

    def stop_rx_thread(self):
        pass
