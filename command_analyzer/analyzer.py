import threading
import time


class CommandAnalyzer:
    def __init__(self):
        print("Command Analyzer Constructor")
        self.command_analyzer_thread = threading.Thread(target=self.analyze, name='AnalyzerThread')
        self.running = True

    def analyze(self):
        time.sleep(10)

    def start_analyzer_thread(self):
        pass

    def stop_analyzer_thread(self):
        pass
