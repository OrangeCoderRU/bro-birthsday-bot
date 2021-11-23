from helpers.utils import validate_date, validate_all_input


def test_user_input_positive_value():
    test_date = "19 September 2000"
    assert validate_date(test_date) != "Error"


def test_user_input_negative_value():
    test_date = "19 Сентября 2000"
    assert validate_date(test_date) is "Error"


def test_all_input_positive_value():
    test_input = "Макс\n03 May 1998"
    assert validate_all_input(test_input) is "Ok"


def test_all_input_negavite_value():
    test_input = "Макс 03 May 1998"
    assert validate_all_input(test_input) is "Error"
