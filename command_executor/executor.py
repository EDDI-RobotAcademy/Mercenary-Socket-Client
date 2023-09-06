import os
import threading
import time


class CommandExecutor:
    def __init__(self, command_queue, transmit_queue):
        print("Command Executor Constructor")
        self.command_executor_thread = threading.Thread(target=self.executor, name='ExecutorThread')
        self.thread_lwp = None
        self.pid = None
        self.running = True
        self.command_executor_queue = command_queue
        self.transmit_response_queue = transmit_queue

    def executor(self):
        self.thread_lwp = threading.current_thread().native_id
        print(f"LWP: {self.thread_lwp}")
        self.pid = os.getpid()
        print(f"Process PID: {self.pid}")
        time.sleep(10)

    def start_executor_thread(self):
        pass

    def stop_executor_thread(self):
        pass
