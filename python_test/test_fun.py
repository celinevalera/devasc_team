import unittest

def fun(x):
  return x+1

class myTest(unittest.TestCase):
  def test(self):
    self.assertEqual(fun(4), 6) #first run N 5, second run 6

if __name__ == "__main__":
  unittest.main()