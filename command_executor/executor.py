import threading
import time




class CommandExecutor:
    def __init__(self):
        print("Command Executor Constructor")
        self.command_executor_thread = threading.Thread(target=self.executor, name='ExecutorThread')
        self.running = True

    def executor(self):
        time.sleep(10)

    def start_executor_thread(self):
        pass

    def stop_executor_thread(self):
        pass
