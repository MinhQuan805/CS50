from datetime import date, timedelta
from seasons import Seasons

def test_valid_date():
    # Test case: Valid date
    year, month, day = "2000", "01", "01"
    result = Seasons.calculate(year, month, day)

    # Calculate expected minutes using timedelta
    today = date.today()
    start = date(int(year), int(month), int(day))
    delta = today - start
    expected_minutes = delta.total_seconds() / 60  # Convert seconds to minutes

    # Assert that the calculated minutes match the expected minutes
    assert result == expected_minutes
