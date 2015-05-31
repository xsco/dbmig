'''
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
'''


class Changelog(object):

    def __init__(self, conn, changeset="default", sql_dialect=None):
        self.conn = conn
        self.changeset = changeset

    def installed(self):
        """ Is a changelog table already installed at the target? """
        cur = self.conn.cursor()
        try:
            cur.execute(
                # TODO - handle other SQL dialects
                """
                SELECT COUNT(*)
                FROM information_schema.tables
                WHERE table_schema = 'public'
                AND table_name = 'dbmig_changelog'
                """)
            row = cur.fetchone()
            return row[0] == 1
        finally:
            cur.close()        

    def version(self):
        """ Return the currently-installed version, or None if none """
        if (not self.installed()):
            return None
        # Fetch the latest version
        cur = self.conn.cursor()
        try:
            cur.execute(
                # TODO - handle other SQL dialects
                """
                SELECT to_version
                FROM dbmig_changelog
                WHERE changeset = %s
                ORDER BY changelog_id DESC
                LIMIT 1
                """,
                (self.changeset,))
            row = cur.fetchone()
            ver = row[0]
            return ver # TODO - convert to SemVer object?
            # There is a package: https://github.com/k-bx/python-semver
        finally:
            cur.close()

