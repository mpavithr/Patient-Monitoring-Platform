import unittest
import deviceAPIwebAppTest1

class TestPhase1(unittest.TestCase):
    def test_checkingForJSON(self):
        result = deviceAPIwebAppTest1.checkingForJSON("devices.json")
        self.assertEqual(result,1)
    def test_checkingEmptyFile(self):
        result = deviceAPIwebAppTest1.checkingEmptyFile("devices.json")
        self.assertEqual(result,1)

        
if __name__ == '__main__':
    unittest.main()
