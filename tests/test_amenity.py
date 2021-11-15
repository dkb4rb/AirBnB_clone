#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class test_Requirements_Amenity(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
