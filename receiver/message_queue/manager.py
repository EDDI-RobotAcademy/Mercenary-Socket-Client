import multiprocessing as mp


class ReceiverCommandDataQueue:
    def __init__(self):
        self.message_queue = mp.Queue()

    def put(self, response):
        self.message_queue.put(response)

    def get(self):
        return self.message_queue.get()

    # 자원 해제
    def close(self):
        self.message_queue.close()

    # 태스크 동작을 보장
    def join(self):
        self.message_queue.join()


if __name__ == "__main__":
    receiver_response_queue = ReceiverCommandDataQueue()

    receiver_response_queue.put((333, "감정 분석 데이터"))
    print("receiver response queue data: ", receiver_response_queue.get())

    receiver_response_queue.close()
