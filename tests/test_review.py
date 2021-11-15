#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.review import Review


class test_Requirements_Review(unittest.TestCase):
    """ Unittest to Holberton Requirements """

    def test_shebang_review(self):
        shebang = "#!/usr/bin/python3"
        f = open("models/review.py", "r")
        for linea in f:
            if shebang == linea:
                print(shebang)
        f.close()

    """  def test_pep8_conformance_review(self):
        fchecker = pep8.Checker('models/review.py', show_source=True)
        file_errors = fchecker.check_all()

        def __str__(self):
            print("\n") """


class TestReview(unittest.TestCase):
    """Testing class Review from models"""

    def test_insistance_Review(self):
        """Test if the data entered is Review type"""
        item = Review()
        self.assertTrue(isinstance(item, BaseModel))

    def test_place_id_review(self):
        """Test if it has place_id attribute"""
        item = Review()
        self.assertTrue(hasattr(item, "place_id"))

    def test_user_id_review(self):
        """Test if it has user_id attribute"""
        item = Review()
        self.assertTrue(hasattr(item, "user_id"))

    def test_text_review(self):
        """Test if it has text attribute"""
        item = Review()
        self.assertTrue(hasattr(item, "text"))


if __name__ == "__main__":
    unittest.main()
