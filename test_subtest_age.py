import unittest
from age import categorize_by_age

def is_even(number):
    return number % 2 == 0

class TestIsEven(unittest.TestCase):
    def test_child_age(self):
        for number in range(0,10):
            with self.subTest(number=number):
                if(self.assertEqual(categorize_by_age(number), "Child") == None):
                    print(number, " is considered as a child")
                else:
                    print(number, " is not considered as a child")

    def test_child_adolescent(self):
        for number in range(10,19):
            with self.subTest(number=number):
                if(self.assertEqual(categorize_by_age(number), "Adolescent") == None):
                    print(number, " is considered as a adolescent")
                else:
                    print(number, " is not considered as a adolescent")

    def test_child_adult(self):
        for number in range(19,66):
            with self.subTest(number=number):
                if(self.assertEqual(categorize_by_age(number), "Adult") == None):
                    print(number, " is considered as a adult")
                else:
                    print(number, " is not considered as a adult")


if __name__ == "__main__":
    unittest.main(verbosity=2)