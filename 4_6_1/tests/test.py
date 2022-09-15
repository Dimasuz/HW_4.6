
import unittest
from unittest.mock import patch
from parameterized import parameterized
import copy
from main import check_document_existance, get_doc_owner_name, delete_doc, add_new_doc
import main


fixture_1 = [('2207 876234', True), ('12345', False)]
fixture_2 = [('10006', 'Аристарх Павлов')]
fixture_3 = ['11-2']
fixture_4 = ('3')

class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        print("setUp ===> START TEST")

    def tearDown(self) -> None:
        print("tearDown ===> STOP TEST")

    @parameterized.expand(fixture_1)
    def test_check_document_existance(self, check_num, answer):
        result = check_document_existance(check_num)
        self.assertEqual(result, answer)

    @parameterized.expand(fixture_2)
    def test_get_doc_owner_name(self, doc_number, name):
        with unittest.mock.patch('builtins.input', return_value=doc_number):
            self.assertEqual(get_doc_owner_name(), name)

    @parameterized.expand(fixture_3)
    def test_delete_doc(self, doc_number):
        documents_check = main.documents.copy()
        directories_check = copy.deepcopy(main.directories)
        with unittest.mock.patch('builtins.input', return_value=doc_number):
            delete_doc()
        self.assertNotEqual(main.documents, documents_check)
        self.assertNotEqual(main.directories, directories_check)
        main.documents = documents_check.copy()
        main.directories = copy.deepcopy(directories_check)


    def test_add_new_doc(self):
        documents_copy = main.documents.copy()
        directories_copy = copy.deepcopy(main.directories)
        documents_check = main.documents.copy()
        val = 'check'
        new_doc = {
            "type": val,
            "number": val,
            "name": val
        }
        documents_check.append(new_doc)
        directories_check = copy.deepcopy(main.directories)
        directories_check[val] = [val]
        with unittest.mock.patch('builtins.input', return_value=val):
            add_new_doc()
        self.assertEqual(main.documents, documents_check)
        self.assertEqual(main.directories, directories_check)
        main.documents = documents_copy.copy()
        main.directories = copy.deepcopy(directories_copy)


if __name__ == '__main__':
    unittest.main()


