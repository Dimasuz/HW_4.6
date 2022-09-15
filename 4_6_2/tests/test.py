
import unittest
from main import create_folder
import main

class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        print("setUp ===> START TEST")

    def tearDown(self) -> None:
        print("tearDown ===> STOP TEST")

    def test_create_folder(self):
        response = create_folder(main.token, main.url, main.folder)
        response.raise_for_status
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()

