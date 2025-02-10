"""
Event Dispatcher Module
This module provides:
    - `EventDispatcher`: A simple event system that allows registering and dispatching events.
    - `register_event(name: str, handler: Callable[[Any], None])`: Registers an event handler.
    - `dispatch_event(name: str, data: Any)`: Dispatches an event to the registered handler.
"""

from typing import Callable, Dict, Any


class EventDispatcher:
    """
     A simple event dispatcher that allows registering and dispatching events.
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        self.events: Dict[str, Callable[[Any], None]] = {}

    def register_event(self, name: str, handler: Callable[[Any], None]) -> None:
        """
        Registers an event handler.
        :param name: The name of the event.
        :param handler: A function to be called when the event is dispatched.
        :raises TypeError: If the handler is not callable.
        """
        if not callable(handler):
            raise TypeError("Handler must be callable")
        self.events[name] = handler

    def dispatch_event(self, name: str, data: Any) -> None:
        """
        Dispatches an event to the registered handler.
        :param name: The name of the event.
        :param data: The data to pass to the event handler.
        :raises KeyError: If the event has not been registered.
        """
        if name not in self.events:
            raise KeyError(f"Event {name} not registered")

        self.events[name](data)


if __name__ == "__main__":
    dispatcher = EventDispatcher()


    def on_message(data: str):
        print(f"Отримано повідомлення: {data}")


    dispatcher.register_event("message", on_message)
    dispatcher.dispatch_event("message", "Привіт!")
