import errno
import socket
import time

from datetime import datetime as dt


class Receiver:
    def __init__(self, receive_queue):
        print("Receiver Constructor")
        self.receiver_command_data_queue = receive_queue

    def start_rx_thread(self, server_socket):
        print("start_rx_thread start!")
        with server_socket:
            while True:
                print("wait for receive data")
                try:
                    data = server_socket.recv(1024)
                    response_str = data.decode().strip()
                    print('{} command received [{}] from server'.format(dt.now(), response_str))

                    self.receiver_command_data_queue.put(response_str)

                except socket.error as e:
                    if e.errno == errno.EWOULDBLOCK:
                        pass

                finally:
                    time.sleep(0.5)

    def stop_rx_thread(self):
        pass
