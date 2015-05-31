"""
    Command-line main() interface for running dbmig operations
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

import sys
import argparse
import dbmig.changelog as changelog
import dbmig.driver_manager as dm

def show(args):
    if args.target == "":
        print("TARGET must be provided for `show' command", file=sys.stderr)
        exit(1)

    conn = dm.connect(args.target)
    cl = changelog.Changelog(conn, args.changeset)
    if args.verbose and not cl.installed():
        print("No changelog table currently exists")

    ver = cl.version()
    if ver is None:
        print("Version installed: (not installed)")
    else:
        print("Version installed: %s" % ver)


def func_not_yet_implemented(args):
    print("`%s' command not yet implemented." % args.command);
    print(commands[args.command]["desc"]);


# Permissible commands and their explanations.
commands = {
    "print-version": {
      "desc": "Print the version",
      "func": func_not_yet_implemented # TODO - NYI
    },
    "show": {
      "desc": "Show the current version",
      "func": show
    },
    "check": {
      "desc": "Check repository integrity with respect to a " +
              "target environment",
      "func": func_not_yet_implemented # TODO - NYI
    },
    "migrate": {
      "desc": "Migrate a target environment to a new version",
      "func": func_not_yet_implemented # TODO - NYI
    },
    "create-unversioned": {
      "desc": "Create an unversioned installation in the target environment",
      "func": func_not_yet_implemented # TODO - NYI
    },
    "override-version": {
      "desc": "Forcibly override the version at the target environment",
      "func": func_not_yet_implemented # TODO - NYI
    },
    "purge": {
      "desc": "Permanently erase the entire contents of a target environment",
      "func": func_not_yet_implemented # TODO - NYI
    }
}

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    
    # Commands accepted as the first positional argument.
    parser.add_argument("command", 
                        choices=commands.keys(),
                        help="the command to execute")
    # Optional arguments that apply in all situations.
    parser.add_argument("-t", "--target", default="",
                        help="target database connection string")
    parser.add_argument("--changeset", default="default",
                        help="name of changeset within target")
    parser.add_argument("-f", "--force", action="store_true",
                        help="do not prompt for confirmation for any operation " +
                             "which modifies the database")
    parser.add_argument("-v", "--verbose", action="count",
                        help="increase output verbosity")
    # Optional arguments for show/check/migrate/create-unversioned.
    parser.add_argument("--repo-dir", default=".",
                        help="path to repository to use (default is " +
                             "current path)")
    # Optional arguments for migrate/override-version.
    parser.add_argument("--version",  default="",
                        help="version to which to migrate target environment")

    args = parser.parse_args()

    # Call the appropriate function based on what command was provided.
    commands[args.command]["func"](args);


if __name__ == "__main__":
    main()

