#!/usr/bin/python3
"""
Test for city
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
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
    
    class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        cy = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cy))
        self.assertNotIn("state_id", cy.__dict__)

    def test_name_is_public_class_attribute(self):
        cy = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cy))
        self.assertNotIn("name", cy.__dict__)

    def test_two_cities_unique_ids(self):
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)

    def test_two_cities_different_created_at(self):
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.created_at, cy2.created_at)

    def test_two_cities_different_updated_at(self):
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.updated_at, cy2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        cystr = cy.__str__()
        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)

if __name__ == "__main__":
    unittest.main()
