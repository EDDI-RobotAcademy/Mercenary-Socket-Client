import queue


class TransmitQueue:
    def __init__(self):
        self.transmit_queue = queue.Queue()

    def put(self, data):
        self.transmit_queue.put(data)

    def get(self):
        return self.transmit_queue.get()


if __name__ == "__main__":
    transmitter_queue = TransmitQueue()

    transmitter_queue.put("분노")
    print("receiver response queue data: ", transmitter_queue.get())
