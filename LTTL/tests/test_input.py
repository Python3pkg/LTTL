"""
Module TestInput.py
Copyright 2016 LangTech Sarl (info@langtech.ch)
-----------------------------------------------------------------------------
This file is part of the LTTL package v2.0

LTTL v2.0 is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

LTTL v2.0 is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with LTTL v2.0. If not, see <http://www.gnu.org/licenses/>.
"""




__version__ = "1.0.0"

import unittest

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from LTTL.Segmentation import Segmentation
from LTTL.Input import Input


class TestInput(unittest.TestCase):
    """Test suite for LTTL Segment module"""

    def setUp(self):
        """ Setting up for the test """
        pass

    def tearDown(self):
        """Cleaning up after the test"""
        pass

    def test_creator(self):
        """Does creator return Input object?"""
        self.assertIsInstance(
            Input(),
            Input,
            msg="creator doesn't return Input object!"
        )

    def test_creator_store_string(self):
        """Does creator store string in class variable?"""
        Input('test')
        self.assertEqual(
            Segmentation.get_data(-1)[:],
            'test',
            msg="creator doesn't store string in class variable!"
        )

    def test_update_string(self):
        """Does update modify stored string?"""
        seg = Input('test2')
        seg.update('modified')
        self.assertEqual(
            Segmentation.get_data(-1)[:],
            'modified',
            msg="update doesn't modify stored string!"
        )

    def test_clear_string(self):
        """Does clear set stored string to None?"""
        seg = Input('test3')
        seg.clear()
        self.assertEqual(
            Segmentation.get_data(-1),
            None,
            msg="clear doesn't set stored string to None!"
        )

    def test_slice_string(self):
        """Does the slicing work like in strings"""
        Input('Hello world!')
        self.assertEqual(
            Segmentation.get_data(-1)[3:7],
            "Hello world!"[3:7],
            msg="slicing doesn't return the same as in strings"
        )


if __name__ == '__main__':
    unittest.main()

