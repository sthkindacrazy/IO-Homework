import sys

BASE_URL = "https://blockchain.info/"
TIMEOUT = 10

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlencode

def call_api(resource, data=None, base_url=BASE_URL):
    try:
        payload = None if data is None else urlencode(data)
        if payload is not None:
            payload = payload.encode('UTF-8')
        response = urlopen(base_url + resource, payload, timeout=TIMEOUT).read()
        return handle_response(response)
            
    except HTTPError as e:
        raise APIException(handle_response(e.read()), e.code)

def handle_response(response):
    return response.decode('UTF-8')
