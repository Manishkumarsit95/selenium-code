import inspect
import logging

class BaseClass:

    def getlogger(self):
      loggerName = inspect.stack()[1][3]
      logger = logging.getLogger(loggerName)
      fileHandlar = logging.FileHandler('logfile.log')

      formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

      fileHandlar.setFormatter(formatter)

      logger.addHandler(fileHandlar)
      logger.setLevel(logging.DEBUG)
      return logger