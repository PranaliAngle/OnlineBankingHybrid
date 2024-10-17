import configparser

config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class Readconfig:


    @staticmethod
    def getApplictionURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUserId():
        loginID=config.get('common info','loginid')
        return loginID

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password

