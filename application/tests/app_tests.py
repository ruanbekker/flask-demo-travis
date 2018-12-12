from run import app
import unittest
import sys
import json

class TestFlaskAppRoot(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_view(self):
        response = self.app.get('/')
        self.assertEqual(
            response.get_data().decode(sys.getdefaultencoding()),
            "Hello, World"
        )

class TestFlaskAppStatus(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_status_view(self):
        response = self.app.get('/status')
        self.assertEqual(
            json.loads(response.get_data().decode(sys.getdefaultencoding())),
            {"status": "OK"}
        )

if __name__ == '__main__':
    unittest.main()
