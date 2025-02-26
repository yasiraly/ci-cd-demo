import unittest
from app import helloworld

class TestApp(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(helloworld(), "Hello World")  # Matches the corrected app.py

if __name__ == "__main__":  # Fixed condition
    unittest.main()
