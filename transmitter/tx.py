import os
import threading
import time


class Transmitter:
    def __init__(self):
        print("Transmitter Constructor")
        self.tx_thread = threading.Thread(target=self.transmit, name='TransmitterThread')
        self.thread_lwp = None
        self.pid = None
        self.running = True

    def transmit(self):
        self.thread_lwp = threading.current_thread().native_id
        print(f"LWP: {self.thread_lwp}")
        self.pid = os.getpid()
        print(f"Process PID: {self.pid}")
        time.sleep(10)

    def start_tx_thread(self):
        self.tx_thread.start()
        pass

    def stop_tx_thread(self):
        pass
