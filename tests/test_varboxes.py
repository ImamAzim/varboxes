#!/usr/bin/env python


"""
test varboxes modules
"""

import os
import unittest


class TestVarBox(unittest.TestCase):

    """all test concerning VarBox. """

    @classmethod
    def setUpClass(cls):
        name = 'test'
        cls.default_parameters = dict(
                a=1,
                b=2,
                c=3,
                )
        cls.parameters = Parameters(name, **cls.default_parameters)

    def test_get_keys(self):
        keys = self.parameters.get_keys()
        self.assertEqual(self.default_parameters.keys(), keys)

    def test_to_dict(self):
        dic = self.parameters.to_dict()
        self.assertDictEqual(self.default_parameters, dic)


""" script tests """


if __name__ == '__main__':
    pass
