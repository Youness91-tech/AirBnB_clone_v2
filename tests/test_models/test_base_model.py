#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        num = self.value()
        self.assertEqual(type(num), self.value)

    def test_kwargs(self):
        """ """
        num = self.value()
        copy = num.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is num)

    def test_kwargs_int(self):
        """ """
        num = self.value()
        copy = num.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        num = self.value()
        num.save()
        key = self.name + "." + num.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], num.to_dict())

    def test_str(self):
        """ """
        num = self.value()
        self.assertEqual(str(num), '[{}] ({}) {}'.format(self.name, num.id,
                         num.__dict__))

    def test_todict(self):
        """ """
        num = self.value()
        n = num.to_dict()
        self.assertEqual(num.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        nw = self.value()
        self.assertEqual(type(nw.id), str)

    def test_created_at(self):
        """ """
        nw = self.value()
        self.assertEqual(type(nw.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        nw = self.value()
        self.assertEqual(type(nw.updated_at), datetime.datetime)
        n = nw.to_dict()
        nw = BaseModel(**n)
        self.assertFalse(nw.created_at == nw.updated_at)
