import re


def log_reader(filename: str):
    """
    Generator function that reads the log file and yields the error code that fits the pattern
    :param filename: the log file to read
    :return: yields the error code
    """
    error_pattern = re.compile(r'\s(4\d{2}|5\d{2})\s')

    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            match = error_pattern.search(line)
            if match:
                yield match.group(1)


def log_writer(output_file: str, input_file: str):
    """
    Function that writes the error code to the output file
    :param output_file: the file to write the error code to
    :param input_file: the file to read the error code from
    """
    with open(output_file, 'w', encoding='UTF-8') as file:
        for error_code in log_reader(input_file):
            file.write(f"{error_code}\n")


if __name__ == '__main__':
    log_writer(output_file='data/task_7_error_codes.txt', input_file='data/sample_log_task_7.txt')
