# -*- coding: utf-8 -*-
"""This module contains test for the helper functions."""
from DAAFi.helpers import list_to_dict


def test_list_to_dict():
    """Test the list_to_dict function."""
    list_2 = [[1, "a"], [2, "b"], [3, "c"]]
    dict_2 = {1: "a", 2: "b", 3: "c"}
    assert list_to_dict(list_2) == dict_2
    list_3 = [[1, "a", "1"], [2, "b", "2"], [3, "c", "3"]]
    assert list_to_dict(list_3) == dict_2
