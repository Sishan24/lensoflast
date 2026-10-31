from datetime import date
from ml.src.date_parsing import parse_numeric_date


def test_unambiguous_day_first_date():
    result = parse_numeric_date("25/12/2027")
    assert result.status == "valid"
    assert result.parsed_date == date(2027, 12, 25)


def test_ambiguous_date_is_not_guessed():
    result = parse_numeric_date("03/04/2027")
    assert result.status == "ambiguous"
    assert result.parsed_date is None


def test_invalid_calendar_date():
    result = parse_numeric_date("31/02/2027")
    assert result.status == "invalid"
