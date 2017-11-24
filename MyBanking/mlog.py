#!/usr/bin/python3

import logging

log_fname = "my_account_app.log"

logging.basicConfig(filename=log_fname,
                    filemode='a',
                    level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def debug(tag, message):
    logging.debug(tag + " : " + message)

def warn(tag, message):
    logging.warning(tag + " : " + message)

def info(tag, message):
    logging.info(tag + " : " + message)

def error(tag, message):
    logging.error(tag + " : " + message)

def critical(tag, message):
    logging.critical(tag + " : " + message)


