#!/usr/bin/python3
"""
Test for user
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser(unittest.TestCase):
    """Testing class user from models"""

    def test_insistance_user(self):
        """Test if the data entered is user type"""
        item = User()
        self.assertIsInstance(item, User)

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

    def test_shebang_user(self):
        shebang = "#!/usr/bin/python3"
        f = open("models/user.py", "r")
        for linea in f:
            if shebang == linea:
                print(shebang)
        f.close()
    
    def test_doctmodule(self):
        """Module is documente"""
        self.assertIsNotNone(User.__doc__)

if __name__ == '__main__':
    unittest.main()
