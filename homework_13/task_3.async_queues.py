"""
Module: async_task_queue
-------------------------
This module demonstrates an asynchronous task queue using `asyncio.Queue`.
"""

import asyncio
import logging

from six import reraise

number_of_consumers = 3
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


async def producer(queue: asyncio.Queue) -> None:
    """
    Produces tasks and adds them to the queue every second.
    :param queue: The asyncio queue where tasks are added.
    :return: None
    :raises asyncio.CancelledError: If the producer task is cancelled.
    :raises Exception: If an unexpected error occurs.
    """
    try:
        for i in range(1, 6):
            await asyncio.sleep(1)
            task = f"Task #{i}"
            await queue.put(task)
            print(f"{task}: was created")

        for i in range(number_of_consumers):
            await queue.put(None)
    except asyncio.CancelledError:
        logging.warning("Producer was cancelled")
        return
    except Exception as e:
        logging.error("Error occurred: %s", e)


async def consumer(queue: asyncio.Queue, consumer_id: int) -> None:
    """
    Consumes tasks from the queue and processes them with a delay.
    :param queue: The asyncio queue to get tasks from.
    :param consumer_id: The ID of the consumer (for logging).
    :return: None
    :raises asyncio.CancelledError: If the consumer task is cancelled.
    :raises Exception: If an unexpected error occurs.
    """
    try:
        while True:
            try:
                task = await queue.get()
            except asyncio.CancelledError:
                logging.warning("Consumer #%d was cancelled", consumer_id)
                raise
            except Exception as e:
                logging.error("Consumer #%d: Failed to retrieve task: %s", consumer_id, e)
                continue

            if task is None:
                logging.info("Consumer #%d received stop signal.", consumer_id)
                break

            print(f"Consumer #{consumer_id}: started working on {task}")
            try:
                await asyncio.sleep(2)
            except asyncio.CancelledError:
                logging.warning("Consumer #%d was cancelled", consumer_id)
                raise

            print(f"Consumer #{consumer_id}: stopped working on {task}")
            queue.task_done()
    except Exception as e:
        logging.error("Error occurred: %s", e)


async def main():
    """
    Runs the producer and multiple consumers asynchronously.
    :return: None
    :raises Exception: If the event loop crashes or tasks fail.
    """
    queue = asyncio.Queue()
    producer_task = asyncio.create_task(producer(queue))

    consumer_tasks = [asyncio.create_task(consumer(queue, i + 1)) for i in range(number_of_consumers)]
    try:
        await asyncio.gather(producer_task, *consumer_tasks)
    except Exception as e:
        logging.error("Error occurred: %s", e)


if __name__ == "__main__":
    asyncio.run(main())
