#!/usr/bin/env python


"""
test varboxes modules
"""

import os
import unittest


from varboxes import VarBox


class TestVarBox(unittest.TestCase):

    """all test concerning VarBox. """

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass


    # @classmethod
    # def setUpClass(cls):
        # cls.varbox = VarBox(name='test_varboxes')

    # def test_get_path(self):
        # varbox = VarBox(name='test_varboxes')

    # def test_get_new_var():
        # pass

    # def test_set_new_var_get_same_session():
        # pass

    # def test_set_new_var_get_diff_session():
        # pass

    # def test_set_old_var_get_same_session():
        # pass

    # def test_set_old_var_get_diff_session():
        # pass


    # def test_get_keys(self):
        # keys = self.parameters.get_keys()
        # self.assertEqual(self.default_parameters.keys(), keys)

    # def test_to_dict(self):
        # dic = self.parameters.to_dict()
        # self.assertDictEqual(self.default_parameters, dic)


""" script tests """


if __name__ == '__main__':
    pass
