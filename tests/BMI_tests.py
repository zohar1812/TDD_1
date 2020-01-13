import unittest
from src import BMI

class BMITest(unittest.TestCase):
    def test_bmi(self):
        # stub
        h1 = 1.8
        w1 = 40
        w2 = 0
        h2 =1.0
        w3 =55
        h3=1.8
        h4=1.8
        w4=78
        h5=1.8
        w5=95
        h6=1.9
        w6=120

        # assume
        expected1 = "severely underweight"
        expected2 = "invalid input"
        expected3 = "underweight"
        expected4 = "Healthy"
        expected5 = "overweight"
        expected6 = "severely overweight"

        # action
        result1 = BMI.bmi_func(h1, w1)
        result2 = BMI.bmi_func(h2, w2)
        result3 = BMI.bmi_func(h3, w3)
        result4 = BMI.bmi_func(h4, w4)
        result5 = BMI.bmi_func(h5, w5)
        result6 = BMI.bmi_func(h6, w6)


        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)
        self.assertEqual(result4, expected4)
        self.assertEqual(result5, expected5)
        self.assertEqual(result6, expected6)


if __name__ == '__main__':
    unittest.main()
