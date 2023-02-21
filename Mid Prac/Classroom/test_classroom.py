import pytest
from classroom import Classroom


@pytest.fixture
def empty_class():
    """We will have a class in room 553 with Tim as instructor"""
    return Classroom("553", "Tim")


@pytest.fixture
def class_with_4_students():
    """
    We will have a class in room 553 with Tim as instructor.
    We also "force" 4 students to be in the class.
    """
    my_class = Classroom("553", "Tim")
    my_class.students = ["John", "Alice", "Ahmed", "Fumiko"]
    return my_class


def test_attributes_constructor():
    """Tests the default values / attributes from the constructor"""
    tims_class = Classroom("552", "Tim")
    assert tims_class.room == "552"
    assert tims_class.instructor == "Tim"
    assert tims_class.students == []


def test_add_student(empty_class):
    empty_class + "John"
    empty_class + "Alice"

    assert "John" in empty_class.students
    assert "Alice" in empty_class.students


def test_len_classroom(class_with_4_students):
    assert len(class_with_4_students) == 4


def test_str(class_with_4_students):
    assert str(class_with_4_students) == "Room 553 [Tim] - 4 students"
