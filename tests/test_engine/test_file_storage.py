#!/usr/bin/python3
import unittest
import os
from datetime import datetime
from time import sleep
import pycodestyle
from models.engine import file_storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import cmd


class FileStorageTests(unittest.TestCase):
    """Represent to new Filestorage Testing"""

    def testFileStorageInstatiation(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_is_an_instance(self):
        """
        Instantiating FileStorages
        """
        Storage = FileStorage()
        self.assertIsInstance(Storage, FileStorage)

    def test_attributes(self):
        """
        Check if the class had corrects attributes
        """
        self.assertTrue(FileStorage, "__file_path")
        self.assertTrue(FileStorage, "__objects")
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "reload"))

    def test_all(self):
        Storage = FileStorage().all()
        self.assertEqual(type(Storage), dict)

    def test_new(self):
        Storage = FileStorage().all()
        self.assertEqual(type(Storage), dict)

    def test_save(self):
        ...

    def test_reload(self):
        ...

    def test_style(self):
        """
        Check if the file had correct style
        """
        pstyle = pycodestyle.StyleGuide(quiet=True)
        result = pstyle.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors.")

if __name__ == "__main__":
    unittest.main()
