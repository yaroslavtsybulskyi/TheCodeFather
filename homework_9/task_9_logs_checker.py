"""
Log checker module
This module provides a function `check_logs` to count all ips in the log record.
"""

import re


def check_logs(filepath: str) -> None:
    """
    Checks logs and counts all correct ips in the log record.
    :param filepath: file path to log file
    :raises FileNotFoundError: if log file does not exist
    :raises TypeError: if log file is not a string
    """
    if not isinstance(filepath, str):
        raise TypeError("filepath must be a string")

    ip_counts = {}

    ip_address_pattern = re.compile(r'\b(?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9]'
                                    r'[0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.'
                                    r'(?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(?:25'
                                    r'[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\b')
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                match = re.search(ip_address_pattern, line)
                if match:
                    ip = match.group()
                    ip_counts[ip] = ip_counts.get(ip, 0) + 1
    except FileNotFoundError:
        print(f"File {filepath} not found.")

    print(f"{filepath} Statistics")
    for ip, count in ip_counts.items():
        print(f"{ip}: {count} times")


if __name__ == "__main__":
    check_logs('task_9_test.txt')
