import unittest
from math_quiz import getRandomInteger, getRandomOperation, resultCalculation


class TestMathGame(unittest.TestCase):

    def test_getRandomInteger(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = getRandomInteger(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_getRandomOperation(self):
        for _ in range(1000):
            randOperation = getRandomOperation()
            self.assertTrue(randOperation == '+' or randOperation == '-' or randOperation == '*')

    def test_function_resultCalculation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (6, 4, '-', '6 - 4', 2),
                (8, 9, '-', '8 - 9', -1),
                (3, 5, '*', '3 * 5', 15),
                (6, 0, '*', '6 * 0', 0)]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problemString, result = resultCalculation(num1, num2, operator)
                self.assertTrue(problemString == expected_problem)
                self.assertTrue(result == expected_answer)

if __name__ == "__main__":
    unittest.main()
