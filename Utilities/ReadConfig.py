# Utilities/ReadConfig.py
import configparser
import os

config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), "config.ini")
config.read(config_path)

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        return config.get("common info", "base_url")

    @staticmethod
    def getUsername():
        return config.get("common info", "username")

    @staticmethod
    def getPassword():
        return config.get("common info", "password")
