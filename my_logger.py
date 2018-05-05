import sys
import os
import logging.config


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # create logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # create a file handler
    logname = os.path.join(os.getcwd(), __name__ + '.log')
    if os.path.exists(logname):
        os.remove(logname)

    file_handler = logging.FileHandler(logname)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # create standard output handler
    std_handler = logging.StreamHandler(sys.stdout)
    std_handler.setLevel(logging.INFO)
    std_handler.setFormatter(formatter)
    logger.addHandler(std_handler)

    # load config from file
    # logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
    # or, for dictConfig
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,  # this fixes the problem
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
        },
        'handlers': {
            'default': {
                'level': 'INFO',            'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            '': {
                'handlers': ['default'],
                'level': 'INFO',
                'propagate': True
            }
        }
    })

    return logger
