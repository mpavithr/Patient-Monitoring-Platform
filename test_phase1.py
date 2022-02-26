import unittest
import test

class TestPhase1(unittest.TestCase):
    def test_checkingForJSON(self):
        result = test.checkingForJSON("devices.json")
        self.assertEqual(result,1)
    def test_checkingEmptyFile(self):
        result = test.checkingEmptyFile("devices.json")
        self.assertEqual(result,1)

        
if __name__ == '__main__':
    unittest.main()
