# Utilities/ReadConfig.py
import configparser
import os

config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), "config.ini")
config.read(config_path)

class ReadConfig:

    @staticmethod
    def getPlatformName():
        return config.get("device info", "platformName")

    @staticmethod
    def getPlatformVersion():
        return config.get("device info", "platformVersion")

    @staticmethod
    def getDeviceName():
        return config.get("device info", "deviceName")

    @staticmethod
    def getAppPath():
        return config.get("device info", "app")

    @staticmethod
    def getAppPackage():
        return config.get("device info", "appPackage")

    @staticmethod
    def getAppActivity():
        return config.get("device info", "appActivity")

    @staticmethod
    def getApplicationURL():
        return config.get("common info", "base_url")

    @staticmethod
    def getUsername():
        return config.get("common info", "username")

    @staticmethod
    def getPassword():
        return config.get("common info", "password")