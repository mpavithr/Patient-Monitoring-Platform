import unittest
import chat_module_unit_tests

class TestPhase1(unittest.TestCase):
    def test_checkingForJSON(self):
        result = chat_module_unit_tests.checkingForJSON("data/chat.txt")
        self.assertEqual(result,0)
    def test_checkingEmptyEntryforFile(self):
        result = chat_module_unit_tests.checkingEmptyEntryforFile(None)
        self.assertEqual(result,0)
    def test_correct_keys_for_chat_json(self):
        result = chat_module_unit_tests.correct_keys_for_chat_json("data/incorrect_keys_chats.json")
        self.assertEqual(result,0)
    def test_correct_value_for_chat_json(self):
        result = chat_module_unit_tests.correct_value_for_chat_json("data/incorrect_values_chats.json")
        self.assertEqual(result,0)

if __name__ == '__main__':
    unittest.main()
