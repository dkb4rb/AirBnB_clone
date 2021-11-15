#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.user import User


class test_Requirements_User(unittest.TestCase):
    """ Unittest to Holberton Requirements """

    def test_shebang_user(self):
        shebang = "#!/usr/bin/python3"
        f = open("models/user.py", "r")
        for linea in f:
            if shebang == linea:
                print(shebang)
        f.close()

    """ def test_pep8_conformance_user(self):
        fchecker = pep8.Checker('models/user.py', show_source=True)
        file_errors = fchecker.check_all()

        def __str__(self):
            print("\n") """


class TestUser(unittest.TestCase):
    """Testing class user from models"""

    def test_insistance_user(self):
        """Test if the data entered is user type"""
        item = User()
        self.assertTrue(isinstance(item, BaseModel))

    def test_email(self):
        """Test if it has email attribute"""
        item = User()
        self.assertTrue(hasattr(item, "email"))

    def test_password(self):
        """Test if it has password attribute"""
        item = User()
        self.assertTrue(hasattr(item, "password"))

    def test_first_name(self):
        """Test if it has first name attribute"""
        item = User()
        self.assertTrue(hasattr(item, "first_name"))

    def test_last_name(self):
        """Test if it has last name attribute"""
        item = User()
        self.assertTrue(hasattr(item, "last_name"))


if __name__ == "__main__":
    unittest.main()
