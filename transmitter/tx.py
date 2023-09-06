import os
import threading
import time


class Transmitter:
    def __init__(self):
        print("Transmitter Constructor")
        self.tx_thread = threading.Thread(target=self.transmit, name='TransmitterThread')
        self.running = True

    def transmit(self):
        # print(threading.current_thread().native_id)
        # print(threading.current_thread().name)
        # print(threading.get_ident())
        # pid = os.getpid()
        # print(f"Process PID: {pid}")
        time.sleep(10)

    def start_tx_thread(self):
        self.tx_thread.start()
        pass

    def stop_tx_thread(self):
        pass
