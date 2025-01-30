def avg_calculator_from_file(filename: str, delimiter: str = None) -> None:
    """
    Calculates the average value from a file.
    :param filename: file to read
    :param delimiter: delimiter of numbers in the file
    """
    total = 0
    count = 0
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            for line in file:
                if delimiter:
                    numbers = line.split(delimiter)
                else:
                    numbers = line.split()

                for number in numbers:
                    try:
                        total += float(number)
                        count += 1
                    except ValueError:
                        print(f"{number} is not a number")
                        continue
            if count != 0:
                print(total / count)
            else:
                print(f"{filename} does not contain digits")
    except FileNotFoundError:
        print(f"{filename} is not found")


if __name__ == "__main__":
    avg_calculator_from_file("data/task_2.txt")
    avg_calculator_from_file("data/task_2_data.txt", delimiter=',')
    avg_calculator_from_file("data/task_2_data_letters.txt")
    avg_calculator_from_file("data/task_2_data_column.txt")
