#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        nw = self.value()
        self.assertEqual(type(nw.state_id), str)

    def test_name(self):
        """ """
        nw = self.value()
        self.assertEqual(type(nw.name), str)
