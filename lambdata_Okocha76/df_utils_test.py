import unittest
from df_utils import lazy_sqrt, builtin_sqrt, newton_sqrt1

class SqrtTests(unittest.TestCase):
    """Tests square root functions"""
    def test_sqrt9(self):
        self.assertEqual(newton_sqrt1(9), 3)
        self.assertEqual(lazy_sqrt(9), 3)
    
    def test_sqrt2(self):
        self.assertAlmostEqual(newton_sqrt1(2), 1.4142135623)
        self.assertAlmostEqual(lazy_sqrt(2), 1.4142135623)
        self.assertAlmostEqual(builtin_sqrt(2), 1.4142135623)

class SquaringTests(unittest.TestCase):
    def test_thing(self):
        pass

if __name__ == '__main__':
    unittest.main()