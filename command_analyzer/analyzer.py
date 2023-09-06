import os
import threading
import time


class CommandAnalyzer:
    def __init__(self, receive_queue, command_queue):
        print("Command Analyzer Constructor")
        self.command_analyzer_thread = threading.Thread(target=self.analyze, name='AnalyzerThread')
        self.thread_lwp = None
        self.pid = None
        self.running = True
        self.receiver_command_data_queue = receive_queue
        self.command_analyzer_queue = command_queue

    def analyze(self):
        self.thread_lwp = threading.current_thread().native_id
        print(f"LWP: {self.thread_lwp}")
        self.pid = os.getpid()
        print(f"Process PID: {self.pid}")
        time.sleep(10)

    def start_analyzer_thread(self):
        pass

    def stop_analyzer_thread(self):
        pass
