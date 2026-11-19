import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_clamp():
    four_spaces_indentation = "    "
    four_spaces_indentation += "assert clamp(3, 1, 10) == 3\n"
    four_spaces_indentation += "assert clamp(15, 1, 10) == 10\n"
    four_spaces_indentation += "assert clamp(0, 1, 10) == 1\n"
    four_spaces_indentation += "assert clamp(5, 1, 10) == 5\n"
    four_spaces_indentation += "assert clamp(-1, 1, 10) == 1\n"
    four_spaces_indentation += "assert clamp(20, 1, 10) == 10\n"
    four_spaces_indentation += "assert clamp(1, 1, 10) == 1\n"
    four_spaces_indentation += "assert clamp(10, 1, 10) == 10\n"
    four_spaces_indentation += "assert clamp(5, 5, 15) == 5\n"
    four_spaces_indentation += "assert clamp(12, 5, 15) == 12\n"
    four_spaces_indentation += "assert clamp(3, 5, 10) == 5\n"
    four_spaces_indentation += "assert clamp(15, 5, 10) == 10\n"
    four_spaces_indentation += "assert clamp(10, 5, 10) == 10\n"
    four_spaces_indentation += "assert clamp(0, 0, 10) == 0\n"
    four_spaces_indentation += "assert clamp(100, 0, 10) == 10\n"
    four_spaces_indentation += "assert clamp(-5
