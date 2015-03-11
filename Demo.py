__author__ = 'JsAndPy'

from Config import *

if __name__ == "__main__":
    LOG4PY = Config.Log4Py
    data = {
        'id': 1,
        'data': 'Hello World'
    }

    LOG4PY.debug('Hello World')
    LOG4PY.info(data)
    LOG4PY.error(data, data)
