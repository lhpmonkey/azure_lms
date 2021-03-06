#!/usr/bin/env python
"""
Command-line utility for administrative tasks.
"""

import os
import sys

try:
    import pymysql
    pymysql.install_as_MySQLdb()
except:
    pass


if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "django_get_started.settings"
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
