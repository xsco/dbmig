"""
    Access a directory containing versioned database scripts
"""
# dbmig - Database schema migration tool
# Copyright (C) 2012-2015  Adam Szmigin (adam.szmigin@xsco.net)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from pathlib import Path

class ScriptDir(object):
    """ Represents a database source code versioned script directory """
    
    def __init__(self):
        pass

# TODO - use sortedcontainers? http://grantjenks.com/docs/sortedcontainers
# (now giving 404)
