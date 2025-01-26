import json


class ConfigManager:
    """
    Configuration Manager Class
    """

    def __init__(self, config_path: str) -> None:
        """Constructor"""
        self.config_path = config_path
        self.config = {}

    def __enter__(self):
        """
        Loading configuration while entering context
        :return: configuration dictionary
        """
        try:
            with open(self.config_path, 'r', encoding='UTF-8') as config_file:
                self.config = json.load(config_file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.config = {}

        return self.config

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Closing configuration while exiting context
        """
        with open(self.config_path, 'w', encoding='UTF-8') as config_file:
            json.dump(self.config, config_file)


if __name__ == '__main__':
    with ConfigManager('data/config.json') as config_file:
        print(config_file)

        config_file['user'] = {'username': 'user',
                               'password': 'password'}
        config_file['drop_db'] = True
        print(config_file)
