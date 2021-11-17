#!/usr/bin/python3
"""
Test for Console
"""
import unittest
import models
import models.engine


class Test_Requirements_Amenity(unittest.TestCase):
    """ Unittest to Holberton Requirements """

    def test_shebang_amenity(self):
        shebang = "#!/usr/bin/python3"
        f = open("models/amenity.py", "r")
        for linea in f:
            if shebang == linea:
                print(shebang)
        f.close()

class Test_Console():
    """Test general about console"""
    def test_quit(self):
        pass

    def test_EOF(self):
        pass

    def test_something(self):
        self.do_something()

if __name__ == "__main__":
    unittest.main()