from nose.tools import assert_true
import requests

class TestUpstreamStatus():
    def test_api_upstream_response(self):
        response = requests.get('https://api.ruanbekker.com/')
        assert_true(response.ok)
