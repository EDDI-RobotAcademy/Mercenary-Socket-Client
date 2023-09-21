import os
import importlib
from protocol.preprocess import prepare_data_for_validation

from inference.age_model import AgeBasedinferringProcessor

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

    # 명령 코드, 파라미터 갯수, 명령 핸들러를 받아서 사용자 정의 AI 명령을 등록
    def register_custom_ai_command(self, command, parameter_count, command_handler):
        self.protocol_command_map[command] = (parameter_count, command_handler)


    # 입력한 데이터가 유효한 사용자 정의 AI 명령인지 확인
    def validate_custom_ai_command(self, received_data):
        command, data_str, parameter_count = prepare_data_for_validation(received_data)
        print(f"command: {command}, data_str: {data_str}, parameter_count: {parameter_count}")

        registered_parameter_count, _ = self.protocol_command_map.get(int(command))

        if registered_parameter_count == parameter_count:
            return True # 있으면 True
        else:
            return False # 없으면 False
        # 예를 들어서 코드에서 '333' 명령이 등록되어 있고 하나의 파라미터를 기대하고 있다면,
        # 파라미터 개수와 '333' 명령을 비교하여 일치하면 유효한 명령이라고 판단.

    # command랑 data 받아와서 명령 실행
    def execute_custom_ai_command(self, command, data):
        _, command_handler = self.protocol_command_map.get(command)

        if not data:
            return command_handler()
        else:
            return command_handler(data[0])

def recommend_card_analysis():
    recommend_card = protocol_manager.execute_custom_ai_command(20, "")

    return recommend_card

    # 이런 식으로 하면 될듯
    # 지금 생각해야 되는 관점은 구지 20,30,40 직접 다 하나씩 함수를 만드는게 아니고 data를 받아와서 그거에 대한 함수를 만들어야함
    # 조금만 생각하면 될거 같은데 너무 졸려서 일단 여기까지하고 나머지는 내일보자


def multi_parameter_test(multi_data):
    return "다중 데이터 요청 성공"

# 여기다 등록하는거야 !!
# AI 명령 등록
# 명령 코드, 파라미터 갯수, 명령 핸들러
protocol_manager = ProtocolManager()
protocol_manager.register_custom_ai_command(555, 3, multi_parameter_test)
protocol_manager.register_custom_ai_command(20, 0, recommend_card_analysis)

# 사용자 정의 명령 핸들러를 가져와 등록
# 위에 거랑 다른 점은 위에 거는 진짜 AI 명령을 등록하는거고
# 아래 거는 외부 모듈에서 가져온 명령어를 등록하는 거임

def learning_command_handler():
    columns = ['age', 'card_id']
    output_file_names = ['age_map_data.xlsx', 'card_number_map_data.xlsx']
    file_path_for_read = '../data/chunk_1-5000.xlsx'
    learning_processor = custom_protocol_importer_module.global_custom_module['age_learn'](columns, output_file_names)
    learning_processor.make_learning_data(file_path_for_read)

def inferring_command_handler():
    processor = AgeBasedinferringProcessor()
    processor.process_data('../data/chunk_1-5000.xlsx')

custom_protocol_importer_module.import_custom_handler()
protocol_manager.register_custom_ai_command(3, 0, learning_command_handler)
protocol_manager.register_custom_ai_command(7, 0, inferring_command_handler)
protocol_manager.register_custom_ai_command(1, 5, recommend_card_analysis)


if __name__ == "__main__":

    recommend_card = protocol_manager.execute_custom_ai_command(20, "")
    print(" 추천된 카드 : ", recommend_card)

