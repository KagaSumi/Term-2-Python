import pytest
from unittest.mock import patch

from models.student import Student


@pytest.fixture
def tim():
    tim = Student("Tim", "A01201234", [24, 86, 70, 74, 58, 57, 81, 41, 75, 49])
    return tim


def test_student_constructor():
    tim = Student("Tim", "A01201234")
    assert tim.name == "Tim"
    assert tim.student_id == "A01201234"
    assert tim.grades == []


def test_student_gpa(tim):
    assert type(Student.gpa) is property
    assert tim.gpa == 61.50
    with patch("builtins.round") as mock_round:
        tim.gpa
        assert mock_round.call_count == 1


def test_student_gpa_no_grades():
    tim = Student("Tim", "A01201234")
    assert tim.gpa == 0


def test_student_to_dict(tim):
    assert tim.to_dict() == {
        "name": "Tim",
        "student_id": "A01201234",
        "grades": [24, 86, 70, 74, 58, 57, 81, 41, 75, 49],
    }
