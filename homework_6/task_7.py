import re


class MessageSender:
    """
    Message Sender Interface
    """

    def send_message(self, message: str):
        """
        Sending the message
        :param message: message text
        """
        pass


class SMSService:
    """
    SMSService class
    """

    def send_sms(self, phone_number: str, message: str):
        """
        Sending the message using sms service
        :param phone_number: phone number to send the message
        :param message: message to send
        """
        phone_number_regex = r'^\+?[1-9]\d{1,14}$'
        if not isinstance(phone_number, str):
            raise TypeError('phone_number must be a string')
        if not isinstance(message, str):
            raise TypeError('message must be a string')
        if not re.match(phone_number_regex, phone_number):
            raise ValueError('phone_number must be a valid phone number')
        print(f"Відправка SMS на {phone_number}: {message}")


class EmailService:
    """
    EmailService class
    """

    def send_email(self, email_address: str, message: str):
        email_address_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not isinstance(email_address, str):
            raise TypeError('email_address must be a string')
        if not isinstance(message, str):
            raise TypeError('message must be a string')
        if not re.match(email_address_regex, email_address):
            raise ValueError('email_address must be a valid email address')
        print(f"Відправка Email на {email_address}: {message}")


class PushService:
    """
    PushService class
    """

    def send_push(self, device_id: str, message: str):
        if not isinstance(device_id, str):
            raise TypeError('device_id must be a string')
        if not isinstance(message, str):
            raise TypeError('message must be a string')
        print(f"Відправка Push-повідомлення на пристрій {device_id}: {message}")


class SMSAdapter(MessageSender):
    """
    SMSAdapter class
    """

    def __init__(self, sms_service: SMSService, phone_number: str) -> None:
        """
        constructor
        :param sms_service: sms service
        :param phone_number: phone number to send message to
        """
        self.sms_service = sms_service
        self.phone_number = phone_number

    def send_message(self, message: str) -> None:
        """
        Sending the message using sms service
        :param message: message to send
        """
        self.sms_service.send_sms(self.phone_number, message)


class EmailAdapter(MessageSender):
    """Email class"""

    def __init__(self, email_service: EmailService, email_address: str) -> None:
        """
        constructor
        :param email_service: email service
        :param email_address: email address
        """
        self.email_service = email_service
        self.email_address = email_address

    def send_message(self, message: str) -> None:
        """
        Sending the message using email service
        :param message: message to send
        """
        self.email_service.send_email(self.email_address, message)


class PushAdapter(MessageSender):
    """
    PushAdapter class
    """

    def __init__(self, push_service: PushService, device_id: str) -> None:
        """
        Constructor
        :param push_service: push service
        :param device_id: device id
        """
        self.push_service = push_service
        self.device_id = device_id

    def send_message(self, message: str) -> None:
        """
        Send the message using push service
        :param message: message to send
        """
        self.push_service.send_push(self.device_id, message)


class MessageSenderSystem:
    """
    MessageSenderSystem class, adapter for all message sender systems
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        self.adapters = []

    def add_adapter(self, adapter: MessageSender) -> None:
        """
        Add adapter to the list of adapters
        :param adapter: name of the adapter
        """
        self.adapters.append(adapter)

    def send_message(self, message: str):
        """
        Send the message using adapter
        :param message: message to send
        """
        for adapter in self.adapters:
            try:
                adapter.send_message(message)
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    sms_service = SMSService()
    email_service = EmailService()
    push_service = PushService()

    sms_adapter = SMSAdapter(sms_service, "+380123456789")
    email_adapter = EmailAdapter(email_service, "user@example.com")
    push_adapter = PushAdapter(push_service, "device123")

    message = "Привіт! Це тестове повідомлення."

    sms_adapter.send_message(message)
    email_adapter.send_message(message)
    push_adapter.send_message(message)

    message_system = MessageSenderSystem()
    message_system.add_adapter(sms_adapter)
    message_system.add_adapter(email_adapter)
    message_system.add_adapter(push_adapter)

    message_system.send_message(message)
