#!/usr/bin/python3
import unittest
import pep8
from models.base_model import BaseModel
from models.state import State

class test_Requirements_State(unittest.TestCase):
    """ Unittest to Holberton Requirements """

    def test_shebang_state(self):
        shebang = "#!/usr/bin/python3"
        f = open("models/state.py", "r")
        for linea in f:
            if shebang == linea:
                print(shebang)
        f.close()

    def test_pep8_conformance_state(self):
        fchecker = pep8.Checker('models/state.py', show_source=True)
        file_errors = fchecker.check_all()

        def __str__(self):
            print("\n")

class TestState(unittest.TestCase):
    """Testing class State from models"""

    def test_insistance_State(self):
        """Test if the data entered is State type"""
        item = State()
        self.assertTrue(isinstance(item, BaseModel))

    def test_name_state(self):
        """Test if it has name attribute"""
        item = State()
        self.assertTrue(hasattr(item, "name"))

if __name__ == "__main__":
    unittest.main()
