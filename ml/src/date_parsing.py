from dataclasses import dataclass
from datetime import date
import re


@dataclass
class ParsedDate:
    raw_text: str
    parsed_date: date | None
    status: str
    reason: str


def parse_numeric_date(raw_text: str, day_first: bool | None = None) -> ParsedDate:
    """Parse only unambiguous numeric dates; do not guess locale.

    day_first=None deliberately rejects ambiguous DD/MM/YYYY-style values.
    """
    text = raw_text.strip()
    match = re.fullmatch(r"(\d{1,2})[./-](\d{1,2})[./-](\d{4})", text)
    if not match:
        return ParsedDate(text, None, "unsupported_or_unrecognised",
                          "Expected a numeric date with a four-digit year.")

    first, second, year = map(int, match.groups())
    if first <= 12 and second <= 12 and first != second and day_first is None:
        return ParsedDate(text, None, "ambiguous",
                          "Both day-first and month-first interpretations are possible.")

    if day_first is True:
        day, month = first, second
    elif day_first is False:
        month, day = first, second
    else:
        # If only one ordering is valid, infer that ordering.
        if first > 12 and second <= 12:
            day, month = first, second
        elif second > 12 and first <= 12:
            month, day = first, second
        else:
            return ParsedDate(text, None, "ambiguous",
                              "Date ordering cannot be established.")

    try:
        return ParsedDate(text, date(year, month, day), "valid", "Parsed using explicit ordering.")
    except ValueError:
        return ParsedDate(text, None, "invalid", "The values do not form a valid calendar date.")
