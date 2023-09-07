import os
import threading
import time

from protocol.manager import protocol_manager


class CommandExecutor:
    def __init__(self, command_queue, transmit_queue):
        print("Command Executor Constructor")
        self.command_executor_thread = threading.Thread(target=self.execute_command, name='ExecutorThread')
        self.thread_lwp = None
        self.pid = None
        self.running = True
        self.command_executor_queue = command_queue
        self.transmit_response_queue = transmit_queue

    def start_executor_thread(self):
        print("start_executor_thread()")
        self.command_executor_thread.start()

    def execute_command(self):
        print("executor thread!")

        while True:
            execution_data = self.command_executor_queue.get()

            command = int(execution_data[0])
            parameter_count = len(execution_data) - 1
            data = execution_data[1:parameter_count + 1]

            response = protocol_manager.execute_custom_ai_command(command, data)
            self.transmit_response_queue.put(response)
            print("Execution request success")

            time.sleep(1)

    def stop_executor_thread(self):
        pass
