from protocol.preprocess import prepare_data_for_validation


class ProtocolManager:
    def __init__(self):
        self.protocol_command_map = {}

    def register_custom_ai_command(self, command, parameter_count, command_handler):
        self.protocol_command_map[command] = (parameter_count, command_handler)

    def validate_custom_ai_command(self, received_data):
        command, data_str, parameter_count = prepare_data_for_validation(received_data)
        print(f"command: {command}, data_str: {data_str}, parameter_count: {parameter_count}")

        registered_parameter_count, _ = self.protocol_command_map.get(int(command))

        if registered_parameter_count == parameter_count:
            return True
        else:
            return False

    def execute_custom_ai_command(self, command, data):
        _, command_handler = self.protocol_command_map.get(command)
        return command_handler(data)


def sentiment_analysis(data):
    return "분노"


def multi_parameter_test(multi_data):
    return "다중 데이터 요청 성공"


protocol_manager = ProtocolManager()
protocol_manager.register_custom_ai_command(333, 1, sentiment_analysis)
protocol_manager.register_custom_ai_command(555, 3, multi_parameter_test)


if __name__ == "__main__":
    def sentiment_analysis(data):
        return "분노"

    protocol_manager = ProtocolManager()
    protocol_manager.register_custom_ai_command(333, 1, sentiment_analysis)

    sentiment = protocol_manager.execute_custom_ai_command(333, "화가 난다")
    print("분석된 감정: ", sentiment)

