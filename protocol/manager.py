class ProtocolManager:
    def __init__(self):
        self.protocol_command_map = {}

    def register_custom_ai_command(self, command, parameter_count, command_handler):
        self.protocol_command_map[command] = (parameter_count, command_handler)

    def execute_custom_ai_command(self, command, data):
        _, command_handler = self.protocol_command_map.get(command)
        return command_handler(data)


if __name__ == "__main__":
    def sentiment_analysis(data):
        return "분노"

    manager = ProtocolManager()
    manager.register_custom_ai_command(333, 1, sentiment_analysis)

    sentiment = manager.execute_custom_ai_command(333, "화가 난다")
    print("분석된 감정: ", sentiment)

