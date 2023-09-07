import os
import queue
import threading
import time


class Transmitter:
    def __init__(self, transmit_queue):
        print("Transmitter Constructor")
        self.tx_thread = threading.Thread(target=self.transmit_response, name='TransmitterThread')
        self.thread_lwp = None
        self.pid = None
        self.running = True
        self.server_socket = None
        self.transmit_response_queue = transmit_queue

    def start_tx_thread(self, server_socket):
        self.server_socket = server_socket
        self.tx_thread.start()

    def transmit_response(self):
        print("transmitter thread!")

        while True:
            # with self.server_socket:
            try:
                response = self.transmit_response_queue.get()

                self.server_socket.sendall(response.encode())
                print("Send response to server success")

            except queue.Empty:
                print("is it operate ? (transmitter)")
                time.sleep(1)

    def stop_tx_thread(self):
        pass
