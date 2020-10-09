'''
Jeremy Kansas
CS 499
Artifact 1 TEST part 2 of 2
'''

import unittest
from rest import stocksRestAPI

class testRestMethods(unittest.TestCase):
    '''
    Very basic beginning of tests for the methods in stocksRestAPI

    *note that url routing is not currently tested
    '''

    def setUp(self):
        self.rest = stocksRestAPI()

    def test_create(self):
        self.assertTrue(self.rest.create("TICKER"))

    def test_read(self):
        self.assertIsInstance(self.rest.read({"Ticker": "BRLI"}), str)

    def test_update(self):
        self.assertIsInstance(self.rest.update({"Ticker": "A"}), str)

    def test_delete(self):
        self.rest.create({"test": "test"})
        self.assertIsInstance(self.rest.delete({"test": "test"}), str)


if __name__ == '__main__':
    unittest.main()
