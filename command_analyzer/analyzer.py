import os
import threading
import time

from protocol.manager import protocol_manager


class CommandAnalyzer:
    def __init__(self, receive_queue, command_queue):
        print("Command Analyzer Constructor")
        self.command_analyzer_thread = threading.Thread(target=self.analyze_command, name='AnalyzerThread')
        self.thread_lwp = None
        self.pid = None
        self.running = True
        self.receiver_command_data_queue = receive_queue
        self.command_analyzer_queue = command_queue

    def start_analyzer_thread(self):
        print("start_analyzer_thread()")
        self.command_analyzer_thread.start()

    def analyze_command(self):
        print("analyzer thread!")
        print("protocol map: ", protocol_manager.protocol_command_map)

        while True:
            received_data = self.receiver_command_data_queue.get()
            if protocol_manager.validate_custom_ai_command(received_data):
                self.command_analyzer_queue = received_data
                print("Success to save command analyzer queue")

            print("received_data: ", received_data)
            time.sleep(1)

    def stop_analyzer_thread(self):
        pass
