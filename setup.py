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

from distutils.core import setup

version = {}
with open(os.path.dirname(os.path.realpath(__file__)) + "/version.py") as fp:
    exec(fp.read(), version)

setup(
    name='dbmig',
    version=version['__version__'],
    author='Adam Szmigin',
    author_email='adam.szmigin@xsco.net',
    scripts=['dbmig-cli.py'],
    packages=['dbmig'],
    license='GNU General Public License v3.0',
    long_description=open('README').read(),
)
