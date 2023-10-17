import unittest
from client3 import getDataPoint, getRatio

class TestClientFunctions(unittest.TestCase):

    def test_getDataPoint(self):
        # Test getDataPoint function with sample data
        quote = {'stock': 'XYZ', 'top_bid': {'price': '100'}, 'top_ask': {'price': '110'}}
        result = getDataPoint(quote)
        self.assertEqual(result, ('XYZ', 100.0, 110.0, 105.0))

    def test_getRatio(self):
        # Test getRatio function with different scenarios
        self.assertEqual(getRatio(10, 5), 2)  # Test positive ratio
        self.assertEqual(getRatio(10, 0), 0)  # Test division by zero, should return 0

if __name__ == '__main__':
    unittest.main()
