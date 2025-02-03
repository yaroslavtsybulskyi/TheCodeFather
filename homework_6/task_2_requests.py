import requests


def save_webpage(url: str, filename: str) -> None:
    """
    Saves the content of a webpage to a specified file.
    :param url: URL of the webpage to download.
    :param filename: The file where the webpage content will be saved.
    :raises requests.exceptions.RequestException: If there is an error during the request.
    """
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(response.text)
        else:
            print(f"Response code: {response.status_code}. Can not save webpage.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    url = 'https://www.google.com/'
    save_webpage(url, 'data/test.txt')
