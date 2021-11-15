#!/usr/bin/python3
"""
Test for amenity
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class Test_Requirements_Amenity(unittest.TestCase):
    """ Unittest to Holberton Requirements """

    def test_shebang_amenity(self):
        shebang = "#!/usr/bin/python3"
        f = open("models/amenity.py", "r")
        for linea in f:
            if shebang == linea:
                print(shebang)
        f.close()

    """ def test_pep8_conformance_amenity(self):
        fchecker = pep8.Checker('models/amenity.py', show_source=True)
        file_errors = fchecker.check_all()

        def __str__(self):
        print("\n") """


class TestAmenity(unittest.TestCase):
    """Testing class Amenity from models"""

    def test_insistance_amenity(self):
        """Test if the data entered is Amenity type"""
        item = Amenity()
        self.assertTrue(isinstance(item, BaseModel))

    def test_name_amenity(self):
        """Test if it has name attribute"""
        item = Amenity()
        self.assertTrue(hasattr(item, "name"))
    
    class TestAmenity_save(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        self.assertLess(first_updated_at, am.updated_at)

    def test_two_saves(self):
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        second_updated_at = am.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        am.save()
        self.assertLess(second_updated_at, am.updated_at)

    def test_save_with_arg(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)

    def test_save_updates_file(self):
        am = Amenity()
        am.save()
        amid = "Amenity." + am.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        am = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())
        self.assertIn("__class__", am.to_dict())

    def test_to_dict_contains_added_attributes(self):
        am = Amenity()
        am.middle_name = "Holberton"
        am.my_number = 98
        self.assertEqual("Holberton", am.middle_name)
        self.assertIn("my_number", am.to_dict())


if __name__ == "__main__":
    unittest.main()
