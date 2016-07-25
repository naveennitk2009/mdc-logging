__author__ = 'naveenkumar'

from django.conf import settings
from mdc_logging.mdc import MDCLogging

mdc_logging = MDCLogging()


class MDCMiddleware(object):

    def process_request(self, request):
        _headers = self.get_headers(request)
        for k, v in _headers.iteritems():
            mdc_logging.set_mdc(k, v)

    @staticmethod
    def get_headers(request):
        _meta = request.META
        _headers = {}
        headers_to_log = settings.HEADERS_TO_LOG
        if headers_to_log is not None:
            for _key in headers_to_log:
                _headers[_key] = _meta.get(_key, "")
        return _headers
