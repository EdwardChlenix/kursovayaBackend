import pytest
import json

import utils

from utils import latest_operations

json_file = 'testfile.json'

def test_open_file():
    assert latest_operations.open_file(json_file) == [{"test1": 1, "test2": 2}]
