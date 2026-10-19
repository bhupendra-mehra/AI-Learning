from learning_utils import clean_text, slugify


def test_clean_text_removes_extra_whitespace():
    assert clean_text("  Hello    Python  ") == "Hello Python"


def test_clean_text_handles_empty_string():
    assert clean_text("") == ""


def test_slugify_converts_text():
    assert slugify("Student Management API") == "student-management-api"


def test_slugify_handles_uppercase():
    assert slugify("PYTHON PACKAGING") == "python-packaging"