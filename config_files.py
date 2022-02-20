import os
from configparser import ConfigParser


class Config:
    def __init__(self):
        self.file = os.path.join(os.path.dirname(__file__), "config.ini")
        if not self.file_exists():
            self.create_file()

    def file_exists(self):
        return os.path.exists(self.file)

    def create_file(self):
        config = ConfigParser()
        config.read(self.file)
        config.add_section('token')
        config.set('token', 'github_token', '')
        with open(self.file, 'w') as configfile:
            config.write(configfile)

    def get_token(self):
        config = ConfigParser()
        config.read(self.file)
        return config['token']['github_token']

    def set_token(self, token):
        config = ConfigParser()
        config.read(self.file)
        config.set('token', 'github_token', token)
        with open(self.file, 'w') as configfile:
            config.write(configfile)

    def is_token_saved(self):
        if self.get_token() == '':
            return False
        return True
