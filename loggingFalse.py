import logging

logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler("test.log")
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('[%(asctime)s][%(thread)d][%(filename)s][line: %(lineno)d][%(levelname)s] ## %(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh)

s = "0"
n = int(s)
logging.info("n = %d" %n)
print(10/n)
