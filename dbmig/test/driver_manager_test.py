#!/usr/bin/env python
"""
    Test the driver_manager module
"""
"""
    dbmig - Database schema migration tool
    Copyright (C) 2012-2015  Adam Szmigin (adam.szmigin@xsco.net)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import unittest
import dbmig.driver_manager as dm

class DriverManagerTestCase(unittest.TestCase):
    """ Tests for the driver_manager module """
    
    def test_invalid(self):
        """ Test behaviour with invalid connection strings """
        with self.assertRaises(dm.NoDriverFoundException):
            dm.parse_driver("")
        with self.assertRaises(dm.InvalidConnectionStringException):
            dm.parse_driver("foo://bar://baz")

    def test_valid(self):
        """ Test behaviour with valid connection strings """
        self.assertEqual(dm.parse_driver("foo://bar"), ("foo", "bar"))


if __name__ == '__main__':
    unittest.main()

