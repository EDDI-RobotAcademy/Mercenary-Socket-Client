import os
import importlib
from protocol.preprocess import prepare_data_for_validation

script_directory = os.path.dirname(__file__)
print("script_directory: ", script_directory)

absolute_module_path = os.path.abspath(os.path.join(script_directory, './custom_protocol_importer'))
print("absolute_module_path: ", absolute_module_path)
relative_module_path = os.path.relpath(absolute_module_path, os.path.abspath(os.getcwd()))
print("relative_module_path: ", relative_module_path)
module_path_for_importlib = relative_module_path.replace(os.path.sep, ".").lstrip(".")
print("module_path_for_importlib: ", module_path_for_importlib)

custom_protocol_importer_module = importlib.import_module(module_path_for_importlib)
# from custom_protocol_importer import import_custom_handler, global_custom_module


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

        if not data:
            return command_handler()
        else:
            return command_handler(data)


def sentiment_analysis(data):
    return "분노"


def multi_parameter_test(multi_data):
    return "다중 데이터 요청 성공"


protocol_manager = ProtocolManager()
protocol_manager.register_custom_ai_command(333, 1, sentiment_analysis)
protocol_manager.register_custom_ai_command(555, 3, multi_parameter_test)

custom_protocol_importer_module.import_custom_handler()
protocol_manager.register_custom_ai_command(3, 0, custom_protocol_importer_module.global_custom_module['salary_learn'])
protocol_manager.register_custom_ai_command(7, 0, custom_protocol_importer_module.global_custom_module['salary_infer'])


if __name__ == "__main__":
    def sentiment_analysis(data):
        return "분노"

    protocol_manager = ProtocolManager()
    protocol_manager.register_custom_ai_command(333, 1, sentiment_analysis)

    sentiment = protocol_manager.execute_custom_ai_command(333, "화가 난다")
    print("분석된 감정: ", sentiment)

