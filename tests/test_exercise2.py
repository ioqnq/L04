import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_is_passing():
    four_spaces_indentation: return grade >= 5
    assert is_passing(5) == True
    assert is_passing(4) == False
    assert is_passing(6) == True


# bug report 2
def test_r2_is_valid_password():
    four_spaces_indentation = "    "
    four_spaces_indentation += "assert is_valid_password(\"abcdefgh\") == True"
    four_spaces_indentation += "    "
    four_spaces_indentation += "assert is_valid_password(\"12345678\") == True"
    four_spaces_indentation += "    "
    four_spaces_indentation += "assert is_valid_password(\"1234567\") == False"
    four_spaces_indentation += "    "
    four_spaces_indentation += "assert is_valid_password(\"abc\") == False"
    four_spaces_indentation += "    "
    four_spaces_indentation += "assert is_valid_password(\"123456789\") == True"
    four_spaces_indentation += "    "
    four_spaces_indentation += "assert is_valid_password(\"12345678a\") == True"
    four_spaces_indentation += "    "
    four_spaces_indentation += "assert is_valid_password(\"12345678a\") == True"
    four_spaces_indentation += "    "
    four_spaces_indentation += "assert is_valid_password(\"12345678a\") == True"
    four_spaces_indentation += "    "
    four_spaces_indentation += "assert is_valid_password(\"12345678a\") == True"
    four_spaces_indentation += "    "
    four_spaces_indentation += "assert is_valid_password(\"12345678a\") == True"
    four_spaces_indentation += "    "
    four_spaces_indentation += "assert is_valid_password(\"12345678a\") == True"
    four_spaces_indentation += "    "
    four_spaces_indentation += "assert is_valid_password(\"12345678a\") == True"
    four_spaces_indentation


# bug report 3
def test_r3_clamp():
    four_spaces_indentation = "    "
    four_spaces_indentation += "assert clamp(10, 1, 5) == 5"
    four_spaces_indentation += "    assert clamp(0, 1, 5) == 1"
    four_spaces_indentation += "    assert clamp(3, 1, 5) == 3"
    four_spaces_indentation += "    assert clamp(-1, 1, 5) == 1"
    four_spaces_indentation += "    assert clamp(6, 1, 5) == 5"
