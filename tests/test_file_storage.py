#!/usr/bin/python3
import unittest
import os
from datetime import datetime
from time import sleep
from models.engine import file_storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import cmd


class FileStorageTests(unittest.TestCase):
    """Represent to new Filestorage Testing"""

    def testFileStorageInstatiation(self):
        self.assertEqual(type(FileStorage()), FileStorage)


if __name__ == "__main__":
    unittest.main()
