import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_hardcoded_admin_password():
    import sqlite3
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (username TEXT, password TEXT)")
    db.execute("INSERT INTO users VALUES ('admin', 'admin123')")
    assert check_admin("admin123") is True
    assert check_admin("wrong") is False


# bug report 2
def test_r2_find_user_sql_injection():
    import sqlite3
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (username TEXT, password TEXT)")
    db.execute("INSERT INTO users VALUES ('admin', 'admin123')")
    assert find_user(db, "admin'; --") is None
