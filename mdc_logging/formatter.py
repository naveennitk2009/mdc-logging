__author__ = 'naveenkumar'

import logging
from mdc_logging.mdc import MDCLogging
import json

mdc_logging = MDCLogging()


class MDCFormatter(logging.Formatter):

    def format(self, record):
        parts = {}
        for k, v in mdc_logging.get_mdc().items():
            p_name = '%s' % k
            parts[p_name] = v
            del p_name
        for x in dir(record):
            if x.startswith('__'):
                continue
            it = getattr(record, x)
            if isinstance(it, str) or isinstance(it, unicode):
                parts[x] = it
            elif 'getMessage' == x:
                parts[x] = record.getMessage()
            else:
                parts[x] = repr(it)
            del it
        result = json.dumps(parts)
        del parts
        # print('format <= %r' % result)
        return result

    def formatException(self, ei):
        result = 'MDC(%r) EXCEPTION=%r' % (mdc_logging.get_mdc(), ei)
        # print('formatException <= %r' % result)
        return result
