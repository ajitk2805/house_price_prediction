from flask import Flask
import sys, os
from housing.logger import logging
from housing.exception import HousingException

application = Flask(__name__)
app = application

@app.route('/', methods=['GET','POST'])
def index():
    try:
        raise Exception('Testing custom exception')
        # logging.info('In app.py')
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info('Testing logging module')
    return "Welcome to Machine Learning Project"

if __name__=='__main__':
    app.run(debug=True)