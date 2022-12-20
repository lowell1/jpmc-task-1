import unittest

from client import getDataPoint, getRatio

class TestGetDataPoint(unittest.TestCase):
    def testGetDataPoint(self):
        quote = {
                'stock': 'ABC', 
                'top_bid': {'price': 100.00}, 
                'top_ask': {'price': 150.00}
            }

        dataPoint = getDataPoint(quote)
        price = dataPoint[3]

        self.assertEqual(price, 125.00)

    def testGetRatio(self):
       self.assertEqual(getRatio(0, 5), 0)
       self.assertEqual(getRatio(2, 5), 0.4)
       self.assertEqual(getRatio(5,0), None)
       self.assertEqual(getRatio(0, 0), None)
       self.assertEqual(getRatio(-1,4), -0.25)


if __name__ == "__main__":
    unittest.main()