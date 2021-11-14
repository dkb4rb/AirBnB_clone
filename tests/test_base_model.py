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

    def test_name_instance(self):
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.created_at, instance2.created_at)

    def test_is_id_exist(self):
        instance1 = BaseModel()
        self.assertTrue(instance1.id)

    def test_if_created_at_exist(self):
        instance1 = BaseModel()
        self.assertTrue(instance1.created_at)

    def test_is_a_dict(self):
        instance1 = BaseModel()
        self.assertEqual(dict, type(instance1.to_dict()))

    def test_atributes_is_a_str(self):
        instance1 = BaseModel()
        self.assertEqual(str, type(instance1.id))


class Test_Types_of_Atributes_Int(unittest.TestCase):

    def test_method_not_is_int(self):
        instance1 = BaseModel()
        self.assertNotEqual(int, type(instance1.to_dict()))

    def test_atribute_not_is_int(self):
        instance1 = BaseModel()
        self.assertNotEqual(int, type(instance1.id))

    def test_atribute_update_at_not_is_int(self):
        instance1 = BaseModel()
        self.assertNotEqual(int, type(instance1.updated_at))

    def test_atribute__crated_at_not_is_int(self):
        instance1 = BaseModel()
        self.assertNotEqual(int, type(instance1.created_at))

    if __name__ == "__main__":
        test_method_not_is_int()
        test_atribute_not_is_int()
        test_atribute_update_at_not_is_int()
        test_atribute__crated_at_not_is_int()


class Test_type_of_atributes_str(unittest.TestCase):

    """ Testing if atributes is str in class BaseModel"""

    def test_atribute_to_dict_no_is_str(self):
        """ if Method to_dict of the class BaseModel not is str"""
        instance1 = BaseModel()
        self.assertNotEqual(str, type(instance1.to_dict))

    def test_method_no_is_str(self):
        """ if Method save the class Basse model not is str """
        instance1 = BaseModel()
        self.assertNotEqual(str, type(instance1.save()))

    """ Main to manage the flow the program """
    if __name__ == "__main__":
        test_atribute_to_dict_no_is_str()
        test_method_no_is_str()


class Test_Instanciate_and_pass_arguments(unittest.TestCase):
    """ Refence to pass arguments """

    def Test_method_save_pass_arguments(self):
        istance1 = BaseModel(None)

    def test_args(self):
        b1 = BaseModel(id=10)
        b2 = BaseModel(id=100)
        self.assertIsNotNone(b1.id, b2.id)


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

        def __str__(self):
            print("\n")

    def test_pep8_conformance2(self):
        fchecker = pep8.Checker('tests/test_base_model.py', show_source=True)
        file_errors = fchecker.check_all()


if __name__ == "__main__":
    unittest.main()
