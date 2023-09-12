import os
import importlib
import inspect

script_directory = os.path.dirname(__file__)
print("exception script_directory: ", script_directory)

global_custom_module = {}


def register_relative_path(relative_path, custom_user_function, function_map_key):
    absolute_module_path = os.path.abspath(os.path.join(script_directory, relative_path))
    print("absolute_module_path: ", absolute_module_path)
    relative_module_path = os.path.relpath(absolute_module_path, os.path.abspath(os.getcwd()))
    print("relative_module_path: ", relative_module_path)
    module_path_for_importlib = relative_module_path.replace(os.path.sep, ".").lstrip(".")
    #module_path_for_importlib += "." + custom_user_function
    print("module_path_for_importlib: ", module_path_for_importlib)

    module = importlib.import_module(module_path_for_importlib)

    if hasattr(module, custom_user_function) and inspect.isfunction(getattr(module, custom_user_function)):
        function_to_register = getattr(module, custom_user_function)
        global_custom_module[function_map_key] = function_to_register


def import_custom_handler():
    relative_location_from_here = [
        "../../../deep_learn/salary/salary_learning",
        "../../../deep_learn/salary/salary_inference",
    ]

    custom_user_function_name = [
        "salary_deep_learn",
        "deep_learn_based_salary_inference",
    ]

    module_function_map_key = [
        "salary_learn",
        "salary_infer",
    ]

    for idx in range(len(relative_location_from_here)):
        register_relative_path(relative_location_from_here[idx],
                               custom_user_function_name[idx],
                               module_function_map_key[idx])



if __name__ == "__main__":
    import_custom_handler()

    global_custom_module['salary_learn']()
    global_custom_module['salary_infer']()


