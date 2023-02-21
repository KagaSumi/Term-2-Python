import pytest
from hangman import show_letters_in_word, all_letters_found

def test_show_letters_1():
    assert show_letters_in_word("Vancouver", ["A", "V"]) == "V A _ _ _ _ V _ _"
    assert show_letters_in_word("Vancouver", ["a", "v"]) == "V A _ _ _ _ V _ _"
    assert show_letters_in_word("TIM", ["G", "V"]) == "_ _ _"
    assert show_letters_in_word("PIZZA", ["A", "I", "P", "Z"]) == "P I Z Z A"

def test_all_letters():
    assert all_letters_found("PIZZA", ["A", "I", "P", "Z"]) is True
    assert all_letters_found("PIZZA", ["A", "I", "P", "Z", "K", "T"]) is True
    assert all_letters_found("VANCOUVER", ["A", "V"]) is False
