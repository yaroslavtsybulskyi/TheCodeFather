"""
Module: async_web_server
-------------------------
This module demonstrates an asynchronous web server using `aiohttp`.
"""

import asyncio
import logging

from aiohttp import web

logging.basicConfig(level=logging.INFO)


async def handle_root(request: web.Request) -> web.Response:
    """
    Handles requests to the root ("/") endpoint.

    :param request: The incoming request object.
    :return: A web response with "Hello, World!".
    :raises web.HTTPMethodNotAllowed: if the requested method is not allowed.
    :raises web.HTTPNotFound: if the web page does not exist.
    :raises TypeError: if the request is not an `aiohttp.web.Request`.
    """
    if not isinstance(request, web.Request):
        raise TypeError('Expected a request object.')

    try:
        if request.method != 'GET':
            raise web.HTTPMethodNotAllowed(method=request.method, allowed_methods=['GET'])
        return web.Response(text='Hello, world')
    except web.HTTPMethodNotAllowed as e:
        logging.error("Method not allowed: %s", e)
        return web.json_response({'message': 'Method not allowed'}, status=405)
    except Exception as e:
        logging.error("Unexpected error: %s", e)
        return web.json_response({'message': 'Unexpected error'}, status=500)


async def handle_slow(request: web.Request) -> web.Response:
    """
    Handles requests to the "/slow" endpoint.

    :param request: The incoming request object.
    :return: A web response with "Operation completed".
    :raises web.HTTPMethodNotAllowed: if the requested method is not allowed.
    :raises TypeError: if the request is not an `aiohttp.web.Request`.
    """
    if not isinstance(request, web.Request):
        raise TypeError('Expected a request object.')

    try:
        if request.method != 'GET':
            raise web.HTTPMethodNotAllowed(method=request.method, allowed_methods=['GET'])
        await asyncio.sleep(5)
        return web.Response(text='Operation Completed!')
    except web.HTTPMethodNotAllowed as e:
        logging.error("Method not allowed: %s", e)
        return web.json_response({'message': 'Method not allowed'}, status=405)
    except Exception as e:
        logging.error("Unexpected error: %s", e)
        return web.json_response({'message': 'Unexpected error'}, status=500)


def create_server() -> web.Application:
    """
    Creates and configures the aiohttp web server with defined routes.
    :return: The aiohttp web application.
    """
    app = web.Application()
    app.router.add_get('/', handle_root)
    app.router.add_get('/slow', handle_slow)
    return app


if __name__ == '__main__':
    try:
        web.run_app(create_server(), port=8080)
    except OSError as e:
        logging.error("Port already in use: %s", e)
    except RuntimeError as e:
        logging.error("Event loop issue: %s", e)
