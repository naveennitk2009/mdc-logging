__author__ = 'naveenkumar'

from django.test import TestCase
import logging
from django.http.response import JsonResponse
from django.test import Client
from mdc_logging.mdc import MDCLogging

logger = logging.getLogger("test_logger")


def header_view(request):
    return JsonResponse({})


class MDCTests(TestCase):

    def test_mdc_method(self):
        try:
            _mdc = MDCLogging()
            _mdc.set_mdc("new_message_key", "Hi I am new message key")
            logger.info("")
        except Exception as e:
            print(e)


    def test_m(self):
        try:
            c = Client(new_header="hello I am new header")
            c.get('/header_test')
            logger.info("")
        except Exception as e:
            print(e)
