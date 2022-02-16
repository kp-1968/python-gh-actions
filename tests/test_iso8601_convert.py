from iso8601_convert import validate_iso_8601_duration_dict
import pytest


def test_validate_iso_8601_not_dict():
    with pytest.raises(TypeError):
        validate_iso_8601_duration_dict(duration='')


def test_validate_iso_8601_months_gt_12():
    vals = {'years': 3, 'months': 13, 'weeks': None, 'days': 4, 'hours': 12, 'minutes': 30, 'seconds': 5}
    with pytest.raises(ValueError, match='Months in a year cannot be greater than 12. Months given = 13'):
        validate_iso_8601_duration_dict(duration=vals)


def test_validate_iso_8601_weeks_gt_5():
    vals = {'years': 3, 'months': 1, 'weeks': 6, 'days': 4, 'hours': 12, 'minutes': 30, 'seconds': 5}
    with pytest.raises(ValueError, match='Weeks in a month cannot be greater than 5. Weeks given = 6'):
        validate_iso_8601_duration_dict(duration=vals)


def test_validate_iso_8601_days_gt_31():
    vals = {'years': 3, 'months': 1, 'weeks': 2, 'days': 32, 'hours': 12, 'minutes': 30, 'seconds': 5}
    with pytest.raises(ValueError, match='Days in a week cannot be greater than 31. Days given = 32'):
        validate_iso_8601_duration_dict(duration=vals)


def test_validate_iso_8601_hours_gt_23():
    vals = {'years': 3, 'months': 1, 'weeks': 2, 'days': 4, 'hours': 24, 'minutes': 30, 'seconds': 5}
    with pytest.raises(ValueError, match='Hours in a day cannot be greater than 23. Hours given = 24'):
        validate_iso_8601_duration_dict(duration=vals)


def test_validate_iso_8601_minutes_gt_59():
    vals = {'years': 3, 'months': 1, 'weeks': 2, 'days': 4, 'hours': 2, 'minutes': 60, 'seconds': 5}
    with pytest.raises(ValueError, match='Minutes in a hour cannot be greater than 59. Minutes given = 60'):
        validate_iso_8601_duration_dict(duration=vals)


def test_validate_iso_8601_seconds_gt_59():
    vals = {'years': 3, 'months': 1, 'weeks': 3, 'days': 4, 'hours': 2, 'minutes': 30, 'seconds': 60}
    with pytest.raises(ValueError, match='Seconds in a minute cannot be greater than 59. Seconds given = 60'):
        validate_iso_8601_duration_dict(duration=vals)
