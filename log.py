import logging

import utils


# Function to save log
def save_log(msg, file):
    formatter = logging.Formatter(
        '%(asctime)s %(message)s', f'{utils.get_datetime()} -')

    # create logger with 'spam_application'
    logger = logging.getLogger('factory')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('log/'+file+'.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    # just so we can see things as they happen in stdout/stderr
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    logger.info(msg)

    logger.removeHandler(fh)
    logger.removeHandler(ch)
