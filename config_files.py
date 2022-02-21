import os
from configparser import ConfigParser


class Config:
    def __init__(self):
        self.file = os.path.join(os.path.dirname(__file__), "config.ini")
        if not self.file_exists():
            self.create_file()

    def file_exists(self):
        """
        Comprueba si un fichero existe
        :return: True si existe, False si no existe
        """
        return os.path.exists(self.file)

    def create_file(self):
        """
        Crea un archivo config.ini, lo llena y lo guarda
        """
        config = ConfigParser()
        config.read(self.file)
        config.add_section('token')
        config.set('token', 'github_token', '')
        with open(self.file, 'w') as configfile:
            config.write(configfile)

    def get_token(self):
        """
        Obtiene el token del archivo ini
        :return: token
        """
        config = ConfigParser()
        config.read(self.file)
        return config['token']['github_token']

    def set_token(self, token):
        """
        Establece un nuevo token
        :param token: nuevo token
        """
        config = ConfigParser()
        config.read(self.file)
        config.set('token', 'github_token', token)
        with open(self.file, 'w') as configfile:
            config.write(configfile)

    def is_token_saved(self):
        """
        Comprueba si hay un token guardado
        :return: True si hay token, False si no hay
        """
        if self.get_token() == '':
            return False
        return True
