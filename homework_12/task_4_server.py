"""
Module: threaded_http_server
----------------------------
This module implements a simple multithreaded HTTP server using Python's built-in
`http.server` module with `ThreadingHTTPServer`.
"""

import logging
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class MyServer(BaseHTTPRequestHandler):
    """
    A simple HTTP request handler for handling GET requests.
    Methods:
        do_GET(): Handles GET requests and responds with a simple text message.
    """

    def do_GET(self) -> None:
        """
        Handles GET requests by responding with "Hello, world!".
        Sends a 200 OK status and a plain text response.

        Response:
            HTTP 200 OK
            Content-Type: text/plain
            Body: "Hello, world!"
        """
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b'Hello, world!')


def run_server(host: str = "localhost", port: int = 8080) -> None:
    """
    Starts multithreaded HTTP server.
    :param host: The hostname or IP address to bind to. Default is "localhost".
    :param port: The port number to listen on. Default is 8080.
    :return: None
    :raises TypeError: If `port` is not an int.
    :raises ValueError: If `host` is not a string.
    """
    if not isinstance(host, str):
        raise TypeError("host must be a string")
    if not isinstance(port, int):
        raise TypeError("port must be a number")

    server_address = (host, port)
    httpd = ThreadingHTTPServer(server_address, MyServer)
    print(f"MyServer is running on http://{server_address[0]}:{server_address[1]}/")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
