"""
HTML tags remover module
This module provides a function `html_tags_remover` to remove all html text from the text.
"""

import re

import requests


def html_tags_remover(text: str) -> str:
    """
    Removes html tags from text
    :param text: text to be processed
    :return: text with html tags removed
    :raises TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError('html_page must be a string')

    pattern = re.compile(r'<.*?>')
    return re.sub(pattern, '', text)


if __name__ == '__main__':
    text = """
<html>
    <head><title>Test Page</title></head>
    <body>
        <h1>Welcome to My Website</h1>
        <p>This is a <b>bold</b> paragraph with some <i>italic</i> text.</p>
        <a href="https://example.com">Click here</a> to visit our page.
        <br>Here is a line break.
        <div class="container">This is inside a div.</div>
    </body>
</html>
"""

    print(html_tags_remover(text))

    response = requests.get('https://google.com')
    print(response.url)
    print(response.text)
    print()
    print('**' * 50)
    print()
    print(html_tags_remover(response.text))
