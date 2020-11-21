from convert_num_to_binary_representation import convert_num_to_binary_representation
import unittest

class Test_Case_Convert_Num_To_Binary_Representation(unittest.TestCase):
    def test_convert_num_to_binary_representation(self):
        self.assertEqual(convert_num_to_binary_representation(0.5), "10000000000000000000000000000000")
        self.assertEqual(convert_num_to_binary_representation(0.644646546456464), "ERROR")