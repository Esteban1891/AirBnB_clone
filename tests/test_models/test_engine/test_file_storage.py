#!/usr/bin/python3
"""File Storage test"""
import unittest
import json
import pep8
import models
import os
import sys

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage"""

    def test_doc_module(self):
        """Module documentation"""
        doc = FileStorage.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_file_storage(self):
        """Test that models/engine/file_storage.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_file_storage(self):
        """Test that tests/test_models/test_engine/test_file_storage.py
        conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        val = 'tests/test_models/test_engine/test_file_storage.py'
        res = pep8style.check_files([val])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = FileStorage.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_init(self):
        """Test constructor"""
        f = FileStorage()
        obj, path = f._FileStorage__objects, f._FileStorage__file_path

        self.assertIsInstance(obj, dict)
        self.assertIsInstance(path, str)

    def test_functions(self):
        """Checks if the functions are defined"""
        f = FileStorage()

        self.assertTrue(hasattr(f, 'all'))
        self.assertTrue(hasattr(f, 'new'))
        self.assertTrue(hasattr(f, 'reload'))
        self.assertTrue(hasattr(f, 'save'))

    def test_all_first(self):
        """Test method all"""
        f = FileStorage()

        self.assertIsInstance(f.all(), dict)

    def setUp(self):
        """Sets up the class test"""

        self.b1 = BaseModel()
        self.a1 = Amenity()
        self.c1 = City()
        self.p1 = Place()
        self.r1 = Review()
        self.s1 = State()
        self.u1 = User()
        self.storage = FileStorage()
        self.storage.save()
        if os.path.exists("file.json"):
            pass
        else:
            os.mknod("file.json")

    def tearDown(self):
        """Tears down the testing environment"""

        del self.b1
        del self.a1
        del self.c1
        del self.p1
        del self.r1
        del self.s1
        del self.u1
        del self.storage
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Check the all"""
        obj = self.storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, self.storage._FileStorage__objects)

    def test_storage_empty(self):
        """check the storage is not empty"""

        self.assertIsNotNone(self.storage.all())

    def test_storage_all_type(self):
        """check the type of storage"""

        self.assertEqual(dict, type(self.storage.all()))

    def test_check_json_loading(self):
        """ Checks if methods from Storage Engine works."""

        with open("file.json") as f:
            dic = json.load(f)

            self.assertEqual(isinstance(dic, dict), True)

    def test_file_existence(self):
        """
        Checks if methods from Storage Engine works.
        """

        with open("file.json") as f:
            self.assertTrue(len(f.read()) > 0)

    def test_docstrings(self):
        """Check the docString each function"""

        self.assertTrue(FileStorage.all.__doc__)
        self.assertTrue(hasattr(FileStorage, 'all'))
        self.assertTrue(FileStorage.new.__doc__)
        self.assertTrue(hasattr(FileStorage, 'new'))
        self.assertTrue(FileStorage.save.__doc__)
        self.assertTrue(hasattr(FileStorage, 'save'))
        self.assertTrue(FileStorage.reload.__doc__)
        self.assertTrue(hasattr(FileStorage, 'reload'))


if __name__ == '__main__':
    unittest.main()
