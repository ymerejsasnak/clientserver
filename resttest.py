import unittest
from rest import stocksRestAPI

class testRestMethods(unittest.TestCase):
    '''
    Test cases for the methods in mongoCRUD class in crud.property

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
        #self.assertIsInstance(self.crud.delete({"test": "test"}), DeleteResult)


if __name__ == '__main__':
    unittest.main()
