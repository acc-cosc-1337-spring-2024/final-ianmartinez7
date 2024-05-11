#write function tests here, don't add input('') statements here!
import unittest
from src.question_a.question_a import find_lowest, find_highest, calculate_total, calculate_average, test_config

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())
#question_a for test case 
class TestQuestionA(unittest.TestCase):
    def test_find_lowest(self):
        
        self.assertEqual(find_lowest([5, 4, 3, 2, 1]), 1)

    def test_find_highest(self):
        
        self.assertEqual(find_highest([5, 4, 3, 2, 1]), 5)

    def test_calculate_total(self):
        
        self.assertEqual(calculate_total([1, 2, 3, 4, 5]), 15)

    def test_calculate_average(self):
        
        self.assertAlmostEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)


#no test case for question_b :)
#no test case for question_c :)
#no test case for question_d


if __name__ == '__main__':
    unittest.main()
