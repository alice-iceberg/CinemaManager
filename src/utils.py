from datetime import datetime


def days_between_datetimes(d1: datetime, d2: datetime) -> int:
    return abs((d1 - d2).days)


# We always return the same date. In a realistic project, you would mock the function instead.
def today() -> datetime:
    return datetime(2023, 11, 24)


def generate_unique_identifier(current=[0]) -> int:
    current[0] += 1
    return current[0]
