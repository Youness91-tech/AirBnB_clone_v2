#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ The class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        dl_list = []
        for key in storage._FileStorage__objects.keys():
            dl_list.append(key)
        for key in dl_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        nw = BaseModel()
        for obj in storage.all().values():
            tmp = obj
        self.assertTrue(tmp is obj)

    def test_all(self):
        """ __objects is properly returned """
        nw = BaseModel()
        tmp = storage.all()
        self.assertIsInstance(tmp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        nw = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        nw = BaseModel()
        thing = nw.to_dict()
        nw.save()
        nw2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        nw = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(nw.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        nw = BaseModel()
        nw.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        nw = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            tmp = key
        self.assertEqual(tmp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)
