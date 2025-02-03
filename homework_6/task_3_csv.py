import csv


def get_average_from_file(filename: str) -> None:
    """
    Calculate and print the average grade from a CSV file.
    :param filename: The name of the CSV file containing student grades.
    :raises FileNotFoundError: If the file does not exist.
    :raises Exception: For any other errors that occur during processing.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            total_grade = 0
            count = 0
            for row in csv_reader:
                total_grade += int(row['Grade'])
                count += 1
            if count > 0:
                print(f"Average grade: {round(total_grade / count, 2)}")
            else:
                print("No students found")
    except FileNotFoundError:
        print("File not found")
    except Exception as error:
        print(f"Error: {error}")


def add_new_student_to_file(filename: str, name: str, age: int, grade: int) -> None:
    """
    Add a new student with name, age, and grade to a CSV file.
    :param filename: The name of the CSV file to add the student to.
    :param name: The name of the student.
    :param age: The age of the student.
    :param grade: The grade of the student.
    :raises Exception: For any errors that occur during file handling.
    """
    try:
        with open(filename, 'a', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['name', 'age', 'grade'])
            writer.writerow({'name': name, 'age': age, 'grade': grade})
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    get_average_from_file('data/task_3_data.csv')
    add_new_student_to_file('data/task_3_data.csv', 'Jim', 26, 4)
    get_average_from_file('data/task_3_data.csv')
