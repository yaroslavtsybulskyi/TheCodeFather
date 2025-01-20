import importlib
import inspect


def analyze_module(module_name: str) -> None:
    """
    Function to analyze the module by given name
    :param module_name:  the name of the module to be analyzed
    """
    try:
        module = importlib.import_module(module_name)

        functions = inspect.getmembers(module, inspect.isroutine)
        if functions:
            print(f"{module_name.capitalize()} functions:")
            for name, func in functions:
                try:
                    signature = inspect.signature(func)
                    formatted_signature = str(signature).replace(", /", "")
                    print(f"{name}: {formatted_signature}")
                except ValueError:
                    print(f"{name}: <signature is not available>")
        else:
            print(f"{module_name.capitalize()} does not have any functions")

        print('*' * 40)
        classes = inspect.getmembers(module, inspect.isclass)
        if classes:
            print(f"{module_name.capitalize()} classes:")
            for name, cls in classes:
                print(f"{name}")
        else:
            print(f"{module_name.capitalize()} does not have any classes")

    except ModuleNotFoundError:
        print(f"Module {module_name} not found.")


if __name__ == '__main__':
    analyze_module("math")
