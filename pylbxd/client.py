import hashlib
import hmac
import time
import uuid

import requests

from .constants import BASE_URL


class Client(object):
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.session = self._create_session()

    def _create_session(self):
        session = requests.Session()
        session.params.update(self._get_default_params())
        session.headers.update(self._get_default_headers())
        return session

    def _get_default_params(self):
        return {'apikey': self.key}

    @staticmethod
    def _get_default_headers():
        return {'Accept': 'application/json',
                'Content-Type': 'application/json'}

    def request(self, method, path, params=None, headers=None, body=None):
        return self.session.request(
                method=method, url=self._get_url(path), params=params,
                headers=headers, data=body,
                auth=Auth(self.key, self.secret, token=self._get_token()))

    @staticmethod
    def _get_url(path):
        return requests.compat.urljoin(BASE_URL, path)

    def _get_token(self):
        return getattr(self, 'token', None)


class Auth(requests.auth.AuthBase):
    def __init__(self, key, secret, token=None):
        self.key = key
        self.secret = secret
        self.token = token

    def __call__(self, request):
        stamp = self._get_stamp()
        request.prepare_url(request.url, stamp)
        signature = self._get_signature(
                self.secret, request.method,
                request.url, getattr(request, 'body', None))
        request.prepare_url(request.url, {'signature': signature})
        if self.token:
            request.headers['Authorization'] = 'Bearer %s' % self.token
        else:
            request.headers['Authorization'] = 'Signature %s' % signature
        return request

    @staticmethod
    def _get_stamp():
        return {'nonce': str(uuid.uuid4()), 'timestamp': int(time.time())}

    @classmethod
    def _get_signature(cls, secret, method, url, body):
        signature = hmac.new(
                key=secret.encode(),
                msg=cls._get_salted_string(method, url, body).encode(),
                digestmod=hashlib.sha256)
        return signature.hexdigest()

    @staticmethod
    def _get_salted_string(method, url, body=None):
        return '{method}\u0000{url}\u0000{body}'.format(
                method=method.upper(), url=url, body=body if body else '')
