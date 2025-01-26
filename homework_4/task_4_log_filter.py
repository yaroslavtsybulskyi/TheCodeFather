def log_filter_generator(input_file: str, keyword: str):
    """
    Generator function that yields log lines from a text file
    :param input_file: file to read the logs from
    :param keyword: keyword to search for
    :return: yields log lines
    """
    with open(input_file, 'r', encoding='UTF-8') as file:
        for line in file:
            if keyword.lower() in line.lower():
                yield line.strip()


def filtered_log_writer(input_file: str, output_file: str, keyword: str):
    """
    Writing filtered log lines to a text file
    :param input_file: file to read the logs from
    :param output_file: file to write the filtered logs to
    :param keyword: keyword to search for

    """
    with open(output_file, 'w', newline='', encoding='UTF-8') as file:
        for line in log_filter_generator(input_file, keyword):
            file.write(line + '\n')


if __name__ == '__main__':
    test = log_filter_generator('data/log_sample.txt', 'info')
    print(next(test))

    filtered_log_writer('data/log_sample.txt', 'data/filtered_log.txt', 'system')
