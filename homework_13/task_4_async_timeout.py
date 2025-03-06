"""
Module: async_timeout_task
--------------------------
This module demonstrates how to use `asyncio.wait_for()` to set a timeout
for an asynchronous task.
"""

import asyncio
import logging

logging.basicConfig(level=logging.INFO)


async def slow_task() -> None:
    """
    Simulates a slow asynchronous task that takes 10 seconds to complete.

    :return: None
    """
    print('Starting slow_task')
    await asyncio.sleep(10)
    print('The task was completed')


async def main() -> None:
    """
    Runs the slow_task() with a timeout of 5 seconds.

    :return: None
    :raises TimeoutError: if the task does not finish within 5 seconds.
    """
    try:
        await asyncio.wait_for(slow_task(), timeout=5)
    except asyncio.TimeoutError:
        logging.error('Timeout! The task was not completed in time')
        return


if __name__ == '__main__':
    asyncio.run(main())
