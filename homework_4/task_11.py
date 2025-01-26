def incremental_avg_calculator(filename: str, delimiter: str = None) -> float:
    """
    Generator that yields the average value from a given file.
    :param filename: the name of the file to read the average value from.
    :param delimiter: delimiter between values in the file.
    :return: average value.
    """
    total = 0
    count = 0

    with open(filename) as file:
        for line in file:
            if delimiter:
                numbers = line.strip().split(delimiter)
            else:
                numbers = [line.strip()]
            for number in numbers:
                try:
                    total += float(number)
                    count += 1
                    yield round(total / count, 2)
                except ValueError:
                    continue


if __name__ == '__main__':
    for item in incremental_avg_calculator('data/task_11_data.txt'):
        print(f"Average: {item}")

    for item in incremental_avg_calculator('data/task_11_data_2.txt', delimiter=','):
        print(f"Average: {item}")
