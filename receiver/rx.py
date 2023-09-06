import errno
import socket
import time

from receiver.message_queue.manager import ReceiverCommandDataQueue

from datetime import datetime as dt


class Receiver:
    def __init__(self):
        print("Receiver Constructor")
        self.receiver_command_data_queue = ReceiverCommandDataQueue()

    def start_rx_thread(self):
        pass

    def stop_rx_thread(self):
        pass

    def receive_command(self, server_socket):
        print("receive_command start!")
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
