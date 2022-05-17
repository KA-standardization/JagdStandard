import logging

logging.basicConfig(level=logging.DEBUG, format='%(thread)d %(threadName)s')


def worker():
    logging.debug('')
    return
