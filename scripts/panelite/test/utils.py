import time


class MaxRetriesExceeded(Exception):
     """Raised if the maximum number of retries has been exceeded"""

class Retrier(object):

    def __init__(self, retries=3, delay=0):
         self.max_retries = retries
         self.delay=delay

         self.retries = 0
         self.acomplished = False

    def __enter__(self):
         return self

    def __exit__(self, exc, value, traceback):
         if not exc:
             self.acomplished = True
             return True
         self.retries += 1
         time.sleep(self.delay)
         if self.retries >= self.max_retries:
             raise MaxRetriesExceeded from exc
         return True
