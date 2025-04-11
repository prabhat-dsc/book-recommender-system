from books_recommender.exception.exception_handler import AppException
from books_recommender.logger.log import logging
import sys

a=10
b=0

def div(a,b):
    try:
        z=a/b
        return z
    except Exception as e:
        logging.info(e)
        raise   AppException(e,sys) from e 
d=div(a,b)
print(d)       

