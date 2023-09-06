import queue

class TransmitQueue:
    def __init__(self):
        self.queue = queue.Queue()

    def put(self, data):
        self.queue.put(data)

    def get(self):
        return self.queue.get()


if __name__ == "__main__":
    transmitter_queue = TransmitQueue()

    transmitter_queue.put("분노")
    print("receiver response queue data: ", transmitter_queue.get())
