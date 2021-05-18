import logging

logging.basicConfig(filename="test.log", filemode='w', level=logging.DEBUG)
logging.debug("this is a debug message ")
logging.info("this is a information message")
logging.error("This is an error message ")
logging.critical("This is a critical message")

