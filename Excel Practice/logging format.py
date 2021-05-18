import logging

logging.basicConfig(filename="test3.log", filemode='w', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m%d%Y %H%M%S')
logging.info("This is an information message ")
logging.warning("This is a warning message ")
logging.error("This is an error message")
logging.critical("This is a critical message ")
