import time

from receiver.message_queue.manager import ReceiverCommandDataQueue

from datetime import datetime as dt


class Receiver:
    def __init__(self):
        print("Receiver Constructor")
        self.receiver_command_data_queue = ReceiverCommandDataQueue()

    def receive_command(self, server_socket):
        print("receive_command start!")
        with server_socket:
            data = server_socket.recv(1024)
            response_str = data.decode().strip()
            print('{} command received [{}] from server'.format(dt.now(), response_str))

            self.receiver_command_data_queue.put(response_str)
            time.sleep(0.05)
