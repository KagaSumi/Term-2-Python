import pytest

from unittest.mock import patch, mock_open
from models.school import School
from models.student import Student

BCIT_JSON = """
{
    "name": "BCIT",
    "students": [
        {
            "name": "Tim",
            "student_id": "A01201234",
            "grades": [24, 86, 70, 74, 58, 57, 81, 41, 75, 49]
        },
        {
            "name": "Bob",
            "student_id": "A09876543",
            "grades": [46, 52, 77, 63, 34, 73, 35, 28, 36, 79]
        }
    ]
}
"""


@pytest.fixture
@patch("builtins.open", new_callable=mock_open, read_data=BCIT_JSON)
def bcit(mock_file):
    s = School("whatever.json")
    return s


def test_constructor():
    """Call load_from_json in the constructor"""
    with patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="{'name': 'BCIT', 'students': []}",
    ) as mock_file:
        with patch("json.load") as mock_json:
            s = School("whatever.json")
            assert mock_file.call_count == 1
            assert "whatever.json" in mock_file.call_args.args
            assert mock_json.call_count == 1


def test_attributes(bcit):
    assert bcit.name == "BCIT"
    assert len(bcit) == 2

    sorted_by_names = bcit.get_students(sorted_by="name")
    sorted_by_gpa = bcit.get_students(sorted_by="gpa")

    assert sorted_by_names[0].name == "Bob"
    assert sorted_by_gpa[0].name == "Tim"


def test_get_student(bcit):
    tim = bcit.get_student("A01201234")
    assert type(tim) == Student
    assert tim.name == "Tim"
    assert tim.student_id == "A01201234"


def test_to_dict(bcit):
    assert bcit.to_dict() == {
        "name": "BCIT",
        "students": [
            {
                "name": "Tim",
                "student_id": "A01201234",
                "grades": [24, 86, 70, 74, 58, 57, 81, 41, 75, 49],
            },
            {
                "name": "Bob",
                "student_id": "A09876543",
                "grades": [46, 52, 77, 63, 34, 73, 35, 28, 36, 79],
            },
        ],
    }


def test_save(bcit):
    with patch("builtins.open", new_callable=mock_open) as mock_file:
        with patch("json.dump") as mock_json:
            bcit.save()
            assert mock_file.call_count == 1
            assert "whatever.json" in mock_file.call_args.args
            assert mock_json.call_count == 1
