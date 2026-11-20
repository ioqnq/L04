import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_is_passing():
    four_spaces_indentation: 4
    assert is_passing(5) == True
    assert is_passing(6) == True
    assert is_passing(4) == False


# bug report 2
def test_r2_is_valid_password():
    assert is_valid_password("password1") == True


# bug report 3
def test_r3_clamp():
    assert clamp(10, 1, 5) == 5
