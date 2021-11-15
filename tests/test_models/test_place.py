#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.place import Place


class test_Requirements_Place(unittest.TestCase):
    """ Unittest to Holberton Requirements """

    def test_shebang_place(self):
        shebang = "#!/usr/bin/python3"
        f = open("models/place.py", "r")
        for linea in f:
            if shebang == linea:
                print(shebang)
        f.close()

    """ def test_pep8_conformance_place(self):
        fchecker = pep8.Checker('models/place.py', show_source=True)
        file_errors = fchecker.check_all()

        def __str__(self):
            print("\n") """


class TestPlace(unittest.TestCase):
    """Testing class Place from models"""

    def test_insistance_place(self):
        """Test if the data entered is Place type"""
        item = Place()
        self.assertTrue(isinstance(item, BaseModel))

    def test_city_id_place(self):
        """Test if it has city_id attribute"""
        item = Place()
        self.assertTrue(hasattr(item, "city_id"))

    def test_user_id_place(self):
        """Test if it has user_id attribute"""
        item = Place()
        self.assertTrue(hasattr(item, "user_id"))

    def test_name_place(self):
        """Test if it has name attribute"""
        item = Place()
        self.assertTrue(hasattr(item, "name"))

    def test_description_place(self):
        """Test if it has description attribute"""
        item = Place()
        self.assertTrue(hasattr(item, "description"))

    def test_number_rooms_place(self):
        """Test if it has number_rooms attribute"""
        item = Place()
        self.assertTrue(hasattr(item, "number_rooms"))

    def test_number_bathrooms_place(self):
        """Test if it has number_bathrooms attribute"""
        item = Place()
        self.assertTrue(hasattr(item, "number_bathrooms"))

    def test_max_guest_place(self):
        """Test if it has max_guest attribute"""
        item = Place()
        self.assertTrue(hasattr(item, "max_guest"))

    def test_price_by_night_place(self):
        """Test if it has price_by_night attribute"""
        item = Place()
        self.assertTrue(hasattr(item, "price_by_night"))

    def test_latitude_place(self):
        """Test if it has latitude attribute"""
        item = Place()
        self.assertTrue(hasattr(item, "latitude"))

    def test_longitude_place(self):
        """Test if it has longitude attribute"""
        item = Place()
        self.assertTrue(hasattr(item, "longitude"))

    def test_amenity_ids_place(self):
        """Test if it has lamenity_ids attribute"""
        item = Place()
        self.assertTrue(hasattr(item, "amenity_ids"))


if __name__ == "__main__":
    unittest.main()
