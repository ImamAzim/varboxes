#!/usr/bin/env python


"""
test varboxes modules
"""

import os
import unittest
import time


from varboxes import VarBox


class TestVarBox(unittest.TestCase):

    """all test concerning VarBox. """

    @classmethod
    def setUpClass(cls):
        cls.varbox = VarBox(app_name='test_varbox')

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # def test_new(self):
        # self.varbox.new('test_var')

    # def test_get_new_var(self):
        # new_var_name = str(time.time_ns())
        # with self.assertRaises(AttributeError):
            # getattr(self, new_var_name)

    # def test_set(self):
        # varbox1
        # newvarname
        # newvalue
        # varbox1.newvarname=newvalue
        # assert equal
        # varbox2
        # assert equal
        # del value

    # def test_del(self):
        # # varbox1
        # # newvarname
        # # newvalue
        # # varbox1.newvarname=newvalue
        # del varbox1.newvarname
        # # assert not exist
        # # varbox2
        # # assert not exist
        # if exist, print check variables




    # def test_get_path(self):
        # varbox = VarBox(name='test_varboxes')


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

# def test_set_get_vars():
    # varbox1 = VarBox(app_name='test_varbox')
    # new_var_name = str(time.time_ns())



if __name__ == '__main__':
    pass
