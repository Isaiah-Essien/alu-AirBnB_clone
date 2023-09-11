#!/usr/bin/python3

"""Unittest for Amenity Class."""

import unittest

from models.amenity import Amenity

from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for  Amenity class."""

    def test_class(self):
        """test instantiation and attributes"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)
        self.assertIn("id", amenity.__dict__)
        self.assertIn("created_at", amenity.__dict__)
        self.assertIn("updated_at", amenity.__dict__)
        self.assertIn("name", Amenity.__dict__)
        self.assertEqual(Amenity.name, "")
        self.assertEqual(amenity.name, "")

    # def test_instance(self):
    #     """test instance."""
    #     amenity = Amenity()
    #     self.assertIsInstance(amenity, Amenity)

    # def test_is_class(self):
    #     """test instance."""
    #     amenity = Amenity()
    #     self.assertEqual(str(type(amenity)),
    #                      "<class 'models.amenity.Amenity'>")

    # def test_is_subclass(self):
    #     """test is_subclass."""
    #     amenity = Amenity()
    #     self.assertIn(amenity, BaseModel)

    # def test_attr(self):
    #     """test is_subclass."""
    #     amenity = Amenity()
    #     self.assertEqual(amenity.name, "")
    #     self.assertEqual(Amenity.name, "")
