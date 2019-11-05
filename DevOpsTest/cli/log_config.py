import sys


def get_log_config(log_level: str):
    console_handler = 'console'
    null_handler = 'null_handler'

    silence_logs = log_level == 'OFF'
    if log_level == 'OFF':
        # we need some valid value
        log_level = 'CRITICAL'

    active_handler = null_handler if silence_logs else console_handler

    log_debug = {
        'handlers': [active_handler],
        'level': 'DEBUG',
        'propagate': False
    }
    log_warning = {
        'handlers': [active_handler],
        'level': 'WARNING',
        'propagate': False
    }

    return {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            console_handler: {
                'level': log_level,
                'class': 'logging.StreamHandler',
                'formatter': 'console_formatter',
                'stream': sys.stderr
            },
            null_handler: {
                'level': 'CRITICAL',
                'class': 'logging.NullHandler'
            }
        },
        'loggers': {
            '': {
                'handlers': [active_handler],
                'level': 'INFO',
            },
            'atlassiansrecli': log_debug,
            'datadog.api': log_warning,
            'signalfx': log_warning,
        },
        'formatters': {
            'console_formatter': {
                'format': '%(levelname)s: %(message)s'
            }
        }
    }
