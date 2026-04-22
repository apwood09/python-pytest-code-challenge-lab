import pytest
from palindrome import longest_palindromic_substring

# basic
def test_basic_palindromes(): 
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"
    assert longest_palindromic_substring("racecar") == "racecar"

# edge cases
def test_edge_cases(): 
    # single character
    assert longest_palindromic_substring("a") == "a"

    # empty string
    assert longest_palindromic_substring("") == ""

    # two diff characters 
    assert longest_palindromic_substring("ab") in ["a", "b"]

    # same characters
    assert longest_palindromic_substring("aaa") == "aaa"

# non alphanumeric 
def test_non_alphanumeric(): 
    assert longest_palindromic_substring("12321") == "12321"
    assert longest_palindromic_substring("aba$aba") == "aba$aba"

# performance 
def test_performance(): 
    # large string
    large_input = "a" * 1000
    assert longest_palindromic_substring(large_input) == "a" * 1000

# longer than one character 
def test_no_palindrome_longer_than_one():
    assert len(longest_palindromic_substring("abcde")) == 1