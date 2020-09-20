import unittest
from crud import mongoCRUD
from pymongo.results import DeleteResult

class testMongoCrudMethods(unittest.TestCase):
    '''
    Test cases for the methods in mongoCRUD class in crud.property
    '''

    def setUp(self):
        self.crud = mongoCRUD()

    def test_create(self):
        self.assertTrue(self.crud.create({"CREATE": "newdoc"}))
        self.assertFalse(self.crud.create("CREATE"))

    def test_read(self):
        self.assertIsInstance(self.crud.read({"Ticker": "BRLI"}), str)

    def test_update(self):
        self.assertIsInstance(self.crud.update({"Ticker": "A"}, {"newkey": "newvalue"}), str)

    def test_delete(self):
        self.crud.create({"test": "test"})
        self.assertIsInstance(self.crud.delete({"test": "test"}), DeleteResult)


if __name__ == '__main__':
    unittest.main()
