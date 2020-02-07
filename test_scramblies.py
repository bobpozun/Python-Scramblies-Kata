#!python3

import pytest


def scramble(s1, s2):
    # code here
    result = True

    return result


class Test:
    testdata = [
        ("rkqodlw", "world", True),
        ("cedewaraaossoqqyt", "codewars", True),
        ("katas", "steak", False),
        ("thonyx", "python", False),
        ("thoningpy", "python", True),
        ("sthonpy", "pythons", True),
        ("pyhons", "python", False),
        ("aabbcamaomsccdd", "commas", True),
        ("commas", "commas", True),
        ("sammoc", "commas", True)
    ]

    @pytest.mark.parametrize('str1, str2, expected', testdata)
    def test(self, str1, str2, expected):
        assert (scramble(str1,str2) == expected)