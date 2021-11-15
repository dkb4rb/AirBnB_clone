#!/usr/bin/python3
"""
Test for user
"""
import models.user
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Testing class user from models"""

    def test_insistance_User(self):
        """Test if the data entered is User type"""
        item = User()
        self.assertTrue(isinstance(item, BaseModel))

    def test_email(self):
        """Test if it has email attribute"""
        item = User()
        date = getattr(item, "email")
        self.assertIsInstance(date, str)

    def test_password(self):
        """Test if it has password attribute"""
        item = User()
        date = getattr(item, "password" )
        self.assertIsInstance(date, str)

    def test_first_name(self):
        """Test if it has first name attribute"""
        item = User()
        date = getattr(item, "first_name")
        self.assertIsInstance(date, str)

    def test_last_name(self):
        """Test if it has last name attribute"""
        item = User()
        date = getattr(item, "last_name")
        self.assertIsInstance(date, str)
    
    def test_doctmodule(self):
        """Module is documented"""
        self.assertIsNotNone(models.user.__doc__)
    
    def test_doctclass(self):
        """Class is documente"""
        self.assertIsNotNone(User.__doc__)   

    def test_if_inheritance_to_BaseModel(self):
        "Test if user class is inheritance from BaseModel"
        item = type(self.user)
        self.assertTrue(issubclass(item, BaseModel))

class Test_Requirements_State(unittest.TestCase):
    """ Unittest to Holberton Requirements """

    def test_shebang_user(self):
        shebang = "#!/usr/bin/python3"
        f = open("models/user.py", "r")
        for linea in f:
            if shebang == linea:
                print(shebang)
        f.close()

if __name__ == '__main__':
    unittest.main()
