import requests


def save_webpage(url: str, filename: str) -> None:
    """
    Saves a webpage to a file.
    :param url: webpage url to save
    :param filename: file to save to
    """
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(response.text)
        else:
            print(f"Response code: {response.status_code}. Can not save webpage.")
    except requests.exceptions.RequestException as e:
        print(e)


if __name__ == '__main__':
    url = 'https://www.google.com/'
    save_webpage(url, 'data/test.txt')
