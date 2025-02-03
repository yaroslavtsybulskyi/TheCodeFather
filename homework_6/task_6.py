import csv
import json
from xml.etree import ElementTree as ET


class CsvToJsonConverter:
    """
    Adapter class to convert csv file to json
    """

    @staticmethod
    def convert_csv_to_json(csv_file_path: str, json_file_path: str) -> None:
        """
        Convert CSV file to JSON.
        :param csv_file_path: The file path of the CSV file.
        :param json_file_path: The file path where the JSON file will be saved.
        :raises FileNotFoundError: If the CSV file is not found.
        """
        try:
            with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                rows = list(csv_reader)

            if not rows:
                print(f"File {csv_file_path} is empty.")
                return

            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(rows, json_file, indent=4)
        except FileNotFoundError:
            print(f'File {csv_file_path} not found')


class JsonToCsvConverter:
    """
    Adapter class to convert json file to csv static method
    """

    @staticmethod
    def convert_json_to_csv(json_file_path: str, csv_file_path: str) -> None:
        """
        Convert JSON file to CSV.
        :param json_file_path: The file path of the JSON file.
        :param csv_file_path: The file path where the CSV file will be saved.
        :raises FileNotFoundError: If the JSON file is not found.
        """
        try:
            with open(json_file_path, 'r', encoding='utf-8') as json_file:
                json_reader = json.load(json_file)

            if not json_reader:
                print(f'File {json_file_path} is empty')
                return

            with open(csv_file_path, 'w', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=json_reader[0].keys())
                writer.writeheader()
                writer.writerows(json_reader)
        except FileNotFoundError:
            print(f'File {json_file_path} not found')


class XmlToJsonConverter:
    """
    Adapter class to convert xml file with known structure (used products from task 5) to json
    """

    @staticmethod
    def convert_xml_to_json(xml_file_path: str, json_file_path: str) -> None:
        """
        Convert XML file to JSON.
        :param xml_file_path: The file path of the XML file.
        :param json_file_path: The file path where the JSON file will be saved.
        :raises FileNotFoundError: If the XML file is not found.
        """
        try:
            tree = ET.parse(xml_file_path)
            root = tree.getroot()

            data = []
            for item in root.findall('product'):
                item_data = {
                    'name': item.find('name').text,
                    'price': item.find('price').text,
                    'quantity': item.find('quantity').text
                }
                data.append(item_data)

            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            print(f'File {xml_file_path} not found')


if __name__ == '__main__':
    CsvToJsonConverter.convert_csv_to_json('data/task_3_data.csv', 'data/task6.json')
    JsonToCsvConverter.convert_json_to_csv('data/task6.json', 'data/task6.csv')
    XmlToJsonConverter.convert_xml_to_json('data/products.xml', 'data/task_6_2.json')
