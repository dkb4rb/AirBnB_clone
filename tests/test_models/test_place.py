#!/usr/bin/python3
"""
Test for place
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place
from models.base_model import BaseModel


class Test_Requirements_Place(unittest.TestCase):
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
       
class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pl))
        self.assertNotIn("city_id", pl.__dict__)

    def test_user_id_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(pl))
        self.assertNotIn("user_id", pl.__dict__)

    def test_name_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(pl))
        self.assertNotIn("name", pl.__dict__)

    def test_description_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(pl))
        self.assertNotIn("desctiption", pl.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(pl))
        self.assertNotIn("number_rooms", pl.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pl))
        self.assertNotIn("number_bathrooms", pl.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(pl))
        self.assertNotIn("max_guest", pl.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(pl))
        self.assertNotIn("price_by_night", pl.__dict__)

    def test_latitude_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(pl))
        self.assertNotIn("latitude", pl.__dict__)

    def test_longitude_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(pl))
        self.assertNotIn("longitude", pl.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(pl))
        self.assertNotIn("amenity_ids", pl.__dict__)

    def test_two_places_unique_ids(self):
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    def test_two_places_different_created_at(self):
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.created_at, pl2.created_at)

    def test_two_places_different_updated_at(self):
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.updated_at, pl2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        pl = Place()
        pl.id = "123456"
        pl.created_at = pl.updated_at = dt
        plstr = pl.__str__()
        self.assertIn("[Place] (123456)", plstr)
        self.assertIn("'id': '123456'", plstr)
        self.assertIn("'created_at': " + dt_repr, plstr)
        self.assertIn("'updated_at': " + dt_repr, plstr)

    def test_args_unused(self):
        pl = Place(None)
        self.assertNotIn(None, pl.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        pl = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(pl.id, "345")
        self.assertEqual(pl.created_at, dt)
        self.assertEqual(pl.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

if __name__ == "__main__":
    unittest.main()
