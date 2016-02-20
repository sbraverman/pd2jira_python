import logging


class BaseClass(object):

    def __init__(self, is_lambda=True):
        self.is_lambda = is_lambda

    def print_error(self, message, e=None):
        result = 'Message: {0}. Error: {1}'.format(message, e)
        if self.is_lambda:
            print result 
        else:
            logging.info(result)
