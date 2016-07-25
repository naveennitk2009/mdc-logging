__author__ = 'naveenkumar'

import threading

local_mdc_thread = None


class MDCLogging(object):

    def __init__(self):
        global local_mdc_thread
        if local_mdc_thread is None:
            local_mdc_thread = threading.local()

    def get_mdc(self):
        k_v_pairs = {}
        for x in dir(local_mdc_thread):
            if x.startswith('__'):
                continue
            k_v_pairs[x] = getattr(local_mdc_thread, x)

        return k_v_pairs

    def set_mdc(self, key, value):
        setattr(local_mdc_thread, key, value)

    def clear_mdc(self):
        for k in self.get_mdc():
            delattr(local_mdc_thread, k)
