import logging

# create logger
logger = logging.getLogger(__name__)
# set log level
logger.setLevel(os.environ.get('LOGLEVEL', 'INFO').upper())
# set formatter
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# add handler
file_handler = logging.FileHandler(os.environ.get('LOGFILE', '/dev/stdout'))
# set formatter for handler
file_handler.setFormatter(formatter)
# add handler to logger
logger.addHandler(file_handler)
# set default log level for specific handler
file_handler.setLevel(logging.ERROR)
# "logging.exception level -- include trace in log"
# log both to file and console with same formatter
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
