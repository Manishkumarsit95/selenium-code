import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)
    fileHandlar = logging.FileHandler('logfile.log')

    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

    fileHandlar.setFormatter(formatter)

    logger.addHandler(fileHandlar)
    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info("Information Statement")
    logger.warning("Somthing is in warring mode")
    logger.error("A major error has happend")
    logger.critical("Critical issue")
