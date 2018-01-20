import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # What happens with to ech message in loggers
    'handlers': {
        'file_all': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, "logs/debug.log"),
        },
        'file_errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, "logs/error.log"),
        }
    },
    # Place for store all messages
    'loggers': {
        'django': {
            'handlers': ['file_all', 'file_errors'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
