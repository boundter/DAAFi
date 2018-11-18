# -*- coding: utf-8 -*-
"""Helper functions to manipulate data."""


def ListToDict(two_dim_list):
    """Convert a 2d-list into a dictionary.

    The key of the dictionary will be the first element of every entry, and the
    value will be the second element. All other elemens will be discarded

    Args:
        two_dim_list (list): The 2d-list to be converted.

    Returns:
        dict: A dictionary of the list.

    Examples:
        >>> input = [[1, "a"], [2, "b"], [3, "b"]]
        >>> ListToDict(input)
        {1: "a", 2: "b", 3: "c"}

    """
    dictionary = {}
    for element in two_dim_list:
        dictionary[element[0]] = element[1]
    return dictionary
