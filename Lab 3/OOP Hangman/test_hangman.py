import pytest
from unittest.mock import patch, mock_open
from hangman import Game


@pytest.fixture
@patch("builtins.open", new_callable=mock_open, read_data="aaaaa")
def game_word_is_a(mock_file):
    return Game(5)


@pytest.fixture
@patch("builtins.open", new_callable=mock_open, read_data="testword")
def game_word_is_testword(mock_file):
    return Game(10)


def test_turns(game_word_is_a):
    # Default value is 10
    assert Game().turns == 10
    
    # This particular game has 5 (see fixture)
    assert game_word_is_a.turns == 5


def test_play_one_round_a(game_word_is_a):
    with patch("builtins.input", return_value="a") as mock_input:
        assert game_word_is_a.play_one_round() is True
        assert game_word_is_a.turns == 4


def test_play_one_round_a_empty_input(game_word_is_a):
    with patch(
        "builtins.input", side_effect=["", "", "", "", "", "", "a", "b"]
    ) as mock_input:
        assert game_word_is_a.play_one_round() is True
        assert game_word_is_a.turns == 4


def test_play_one_round_aa(game_word_is_a):
    with patch("builtins.input", return_value="aa"):
        assert game_word_is_a.play_one_round() is False
        assert game_word_is_a.turns == 4


def test_play_one_round_check(game_word_is_testword):
    with patch("builtins.input", return_value="TESTWORD"):
        assert game_word_is_testword.play_one_round() is True


def test_play_game_a(game_word_is_a):
    with patch(
        "builtins.input", side_effect=["", "", "", "", "", "", "b", "a"]
    ) as mock_input:
        assert game_word_is_a.play() is True
        assert game_word_is_a.turns == 3


def test_play_game_testword_win(game_word_is_testword):
    with patch(
        "builtins.input",
        side_effect=["t", "T", "E", "s", "w", "o", "r", "a", "b", "c", "d"],
    ) as mock_input:
        assert game_word_is_testword.play() is True
        assert game_word_is_testword.turns == 0


def test_play_game_testword_win_goated(game_word_is_testword):
    with patch("builtins.input", side_effect=["dunno", "testWORd"]) as mock_input:
        assert game_word_is_testword.play() is True
        assert game_word_is_testword.turns == 8


def test_play_game_testword_lose(game_word_is_testword):
    with patch(
        "builtins.input", side_effect=["a", "b", "c", "d", "e", "f", "g", "t", "s", "w"]
    ) as mock_input:
        assert game_word_is_testword.play() is False
        assert game_word_is_testword.turns == 0
