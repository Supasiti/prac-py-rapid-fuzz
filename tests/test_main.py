"""Basic tests for the main module."""

from rapidfuzz import fuzz
from prac_py_rapid_fuzz import main


def test_main():

    rapid = int(fuzz.token_set_ratio("monster inc", "monster group"))
    manual = main("monster inc", "monster group")
    assert rapid == manual

    rapid = int(fuzz.token_set_ratio("play school", "kew high school"))
    manual = main("play school", "kew high school")
    assert rapid == manual

