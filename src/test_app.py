import unittest
from main import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_hello(self):
        response = self.client.get('/')
        self.assertEqual(response.data.decode(), "Hello from GCP CI/CD Pipeline!")

    def test_add(self):
        response = self.client.get('/add/2/3')
        self.assertEqual(response.data.decode(), "5")  # adjust as needed

    def test_fail_case(self):
        response = self.client.get('/add/2/2')
        self.assertEqual(response.data.decode(), "4")  # ✅ this should now PASS

if __name__ == '__main__':
    unittest.main()