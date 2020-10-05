#alternate file to bypass need for mongodb for testing purposes
#directly accesses JSON file


import json
from bson import json_util


class crud:
    '''
    Class that implements CRUD functionality on JSON file directly
    since I can't run mongo locally
    '''

    def connect(self, host, port):
        pass


    def set_collection(self, db, col):
        self.data = {}
        with open('stocks.json') as file:
            for line in file:
                json_line = json.loads(line)
                self.data[json_line['Ticker']] = json_line


    def create(self, document):
        '''
        Creates new document in current collection.
        Args:
            document: dictionary of key/value pairs to insert as document
        Returns:
            True on success
            False on failure
        '''
        if document.get('Ticker') is None:
            result = False
        else:
            try:
                self.data[document['Ticker']] = document
                result = True
            except Exception:
                result = False
        return result


    def read(self, query):
        '''
        Reads single document matching passed query document

        Args:
            query: dict key/value pair to use as query

        Returns:
            String dump of JSON document on success
            Exception on failure
        '''

        return self.data[query['Ticker']]


    def update(self, old, new):
        '''
        Updates document matching query "old" with key/value "new"

        Args:
            old: dictionary key/value as query to find in collection
            new: new key/value to add to item

        Returns:
            String dump of JSON document on success
            Exception on failure
        '''
        try:
            doc = self.data[old['Ticker']]
            for key in new:
                doc[key] = new[key]
            result = True
        except Exception as e:
            result = e
        return result


    def delete(self, query):
        '''
        Deletes document matching given query

        Args:
            query: dictionary key/value as query to search for

        Returns:
            DeleteResult on success
            Exception on fail
        '''
        try:
            del self.data[query['Ticker']]
            result = True
        except Exception as e:
            result = e
        return result


if __name__ == '__main__':
    crud = mongoCRUD()
    crud.connect('localhost', 27017)
    crud.set_collection('market', 'stocks')
