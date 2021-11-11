#!/usr/bin/python3
import unittest
import os
import pep8
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_new_instance(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_unique_instance(self):
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_is_id_exist(self):
        instance = BaseModel()
        self.assertTrue(instance.id)

    def test_if_created_at_exist(self):
        instance = BaseModel()
        self.assertTrue(instance.created_at)


class test_Requirements(unittest.TestCase):
    """ Unittest to Holberton Requirements """

    def test_readme(self):
        self.assertTrue(os.path.exists('README.md'))

    def test_shebang(self):
        shebang = "#!/usr/bin/python3"
        f = open("tests/test_base_model.py", "r")
        for linea in f:
            if shebang == linea:
                print(shebang)
        f.close()

    def test_pep8_conformance(self):
        fchecker = pep8.Checker('models/base_model.py', show_source=True)
        file_errors = fchecker.check_all()

    def test_pep8_conformance2(self):
        fchecker = pep8.Checker('tests/test_base_model.py', show_source=True)
        file_errors = fchecker.check_all()


if __name__ == "__main__":
    unittest.main()
