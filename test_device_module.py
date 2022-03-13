import unittest
import device_module_unit_tests

class TestPhase1(unittest.TestCase):
    def test_checkingForJSON(self):
        result = device_module_unit_tests.checkingForJSON("/data/devices.txt")
        self.assertEqual(result,0)
    def test_checkingEmptyEntryforFile(self):
        result = device_module_unit_tests.checkingEmptyEntryforFile(None)
        self.assertEqual(result,0)
    def test_checkingEmptyFile(self):
        result = device_module_unit_tests.checkingEmptyFile("/data/empty_json.json")
        self.assertTrue(result,True)
    def test_correct_keys_for_device_json(self):
        result = device_module_unit_tests.correct_keys_for_device_json("/data/incorrect_keys_devices.json")
        self.assertEqual(result,0)
    def test_incorrect_no_of_keys_device_json(self):
        result = device_module_unit_tests.correct_keys_for_device_json("/data/incorrect_num_keys_device.json")
        self.assertEqual(result,0)
    def test_correct_keys_for_measurement_json(self):
        result = device_module_unit_tests.correct_keys_for_measurement_json("/data/devices.json")
        self.assertEqual(result,0)
    def test_incorrect_no_of_keys_measurement_json(self):
        result = device_module_unit_tests.correct_keys_for_measurement_json("/data/devices.json")
        self.assertEqual(result,0)
    def test_correct_value_for_device_json(self):
        result = device_module_unit_tests.correct_value_for_device_json("/data/incorrect_values_devices.json")
        self.assertEqual(result,0)
    def test_correct_value_for_measurement_json(self):
        result = device_module_unit_tests.correct_value_for_measurement_json("/data/incorrect_values_measurements.json")
        self.assertEqual(result,0)


if __name__ == '__main__':
    unittest.main()
