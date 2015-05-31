"""
    Uniform interface to obtain connections via different DBAPI v2 drivers
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

import re
import importlib

# Maps driver names to importable module names
__driver_to_module_map = {
    "postgresql": "psycopg2"
}

# List of database driver modules already imported
__loaded_drivers = {}


# Custom exceptions
class NoDriverFoundException(Exception):
    """ Indicates no driver delimiter '://' was found in a connection string """
    pass

class UnknownDriverException(Exception):
    """ An unknown database driver """
    pass

class InvalidConnectionStringException(Exception):
    """ Indicates that a connection string was invalid in some way """
    pass


def supported_drivers():
    """ Return a list of supported DB drivers """
    return __driver_to_module_map.keys()

def parse_driver(conn_str):
    """ Parse a connection string to get the database driver
    
    Arguments:
    conn_str -- Connection string, of the form "<driver>://..."
    """
    parts = re.split("://", conn_str);
    if (len(parts) < 2):
        raise NoDriverFoundException(
            "Couldn't find a driver delimiter in the supplied " +
            "connection string '%s'" %
            conn_str);
    if (len(parts) > 2):
        raise InvalidConnectionStringException(
            "Too many driver delimiters in connection string '%s'" %
            conn_str);
    return (parts[0], parts[1])

def connect(conn_str):
    """ Obtain a Database connection
    
    Arguments:
    conn_str -- Connection string, of the form "<driver>://..."
    """
    # Parse the connection string for the database driver
    (driver, partial_conn_str) = parse_driver(conn_str)
    if (driver not in __driver_to_module_map):
        raise UnknownProtocolException("Unknown driver '%s'" % driver)
    importable_name = __driver_to_module_map[driver]
    
    # Import module (if not already imported)
    if (importable_name not in __loaded_drivers):
        m = importlib.import_module(importable_name)
        __loaded_drivers[importable_name] = m
    else:
        m = __loaded_drivers[importable_name]
    
    # Get connection
    return m.connect(partial_conn_str)

