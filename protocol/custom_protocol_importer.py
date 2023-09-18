import os
import importlib
import inspect

script_directory = os.path.dirname(__file__)
print("exception script_directory: ", script_directory)

global_custom_module = {} # 사용자 정의 명령 핸들러 함수 등록하는 딕셔너리

def register_relative_path(relative_path, custom_user_function, function_map_key):
    absolute_module_path = os.path.abspath(os.path.join(script_directory, relative_path))
    print("absolute_module_path: ", absolute_module_path)
    relative_module_path = os.path.relpath(absolute_module_path, os.path.abspath(os.getcwd()))
    print("relative_module_path: ", relative_module_path)
    module_path_for_importlib = relative_module_path.replace(os.path.sep, ".").lstrip(".")
    #module_path_for_importlib += "." + custom_user_function
    print("module_path_for_importlib: ", module_path_for_importlib)

    module = importlib.import_module(module_path_for_importlib)
    # 함수를 사용하여 상대 경로에 있는 모듈을 가져옴

    if hasattr(module, custom_user_function):
        function_or_class = getattr(module, custom_user_function)

        # 클래스 타입인 경우 클래스 인스턴스 등록 (생성자)
				# 실제 함수를 등록 할 수 있도록 에셋을 추가해야하나 우선은 보류하겠음
        if inspect.isclass(function_or_class):
            instance = function_or_class()
            global_custom_module[function_map_key] = instance
        # 함수 타입인 경우 직접 등록
        elif inspect.isfunction(function_or_class):
            global_custom_module[function_map_key] = function_or_class


def import_custom_handler():
    relative_location_from_here = [
        "../../../deep_learn/age/learning_processor",
        "../../../inference/age_model",
    ]

    custom_user_function_name = [
        "make_learning_data",
        "deep_learn_age_model_inference",
    ]

    module_function_map_key = [
        "age_learn",
        "age_infer",
    ]

    for idx in range(len(relative_location_from_here)):
        register_relative_path(relative_location_from_here[idx],
                               custom_user_function_name[idx],
                               module_function_map_key[idx])



if __name__ == "__main__":

    import_custom_handler()

    global_custom_module['age_learn']()
    global_custom_module['age_infer']()


