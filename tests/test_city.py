#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.city import City


class test_Requirements_City(unittest.TestCase):
    """ Unittest to Holberton Requirements """

    def test_shebang_city(self):
        shebang = "#!/usr/bin/python3"
        f = open("models/city.py", "r")
        for linea in f:
            if shebang == linea:
                print(shebang)
        f.close()

    """ def test_pep8_conformance_city(self):
        fchecker = pep8.Checker('models/city.py', show_source=True)
        file_errors = fchecker.check_all()

        def __str__(self):
            print("\n") """


class TestCity(unittest.TestCase):
    """Testing class State from models"""

    def test_insistance_city(self):
        """Test if the data entered is City type"""
        item = City()
        self.assertTrue(isinstance(item, BaseModel))

    def test_state_id_city(self):
        """Test if it has state_id attribute"""
        item = City()
        self.assertTrue(hasattr(item, "state_id"))

    def test_name_city(self):
        """Test if it has name attribute"""

        item = City()
        self.assertTrue(hasattr(item, "name"))


if __name__ == "__main__":
    unittest.main()
