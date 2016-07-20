from logbook import Logger, StreamHandler
import sys


LOG_BASE = 'pikachu'


def logger():
    StreamHandler(sys.stdout).push_application()
    return Logger(LOG_BASE)
