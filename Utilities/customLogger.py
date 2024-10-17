import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        print("hii")
        return logger

