import logging


class LoggingConsole:
    def test_logging(self):
        # creating logger
        logger = logging.getLogger(LoggingConsole.__name__)
        logger.setLevel(logging.DEBUG)
        # creating handler
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.DEBUG)

        # setting the formater
        formatter = logging.Formatter('%(asctime)s: - %(name)s:%(levelname)s:%(message)s', datefmt='%m%d%Y %H%M%S %p')

        # setting the format to handler
        chandler.setFormatter(formatter)

        # setting the handler to logger
        logger.addHandler(chandler)
        # error messages
        logger.debug("This is debug message ")
        logger.info("This is Info message")
        logger.warning("This is a warning message")
        logger.error("This is a error message")
        logger.critical("This is a critical message")


demo = LoggingConsole()
demo.test_logging()
