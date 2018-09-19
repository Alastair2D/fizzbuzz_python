# ___Import Statements___
# import glob
import unittest 
from fizzBuzz import fizzBuzz
# testSuite = unittest.TestSuite()

class FizzBuzzTests(unittest.TestCase):
  
  # def test_fb1_returns_1(self):
  #   result = fizzBuzz(1)
  #   expected = 1  
  #   self.assertEqual(expected, result)

  def test_normal_number(self):
    self.assertEqual(fizzBuzz(1), 1)
    self.assertEqual(fizzBuzz(7), 7)
    self.assertEqual(fizzBuzz(777), 777)

  def test_fizz(self):
    self.assertEqual(fizzBuzz(3), 'fizz')
    self.assertEqual(fizzBuzz(6), 'fizz')
    self.assertEqual(fizzBuzz(999), 'fizz')

  def test_buzz(self):
    self.assertEqual(fizzBuzz(5), 'buzz')
    self.assertEqual(fizzBuzz(10), 'buzz')
    self.assertEqual(fizzBuzz(100), 'buzz')

  def test_multiple_of_3_and_5_should_return_FIZZBUZZ(self):
    self.assertEqual(fizzBuzz(15), 'FIZZBUZZ')
    self.assertEqual(fizzBuzz(30), 'FIZZBUZZ')


  # def main():
  #   unittest.main()

# ____Run the tests____
 if __name__ == '__main__':
    unittest.main()   