import datetime as dt

foundation_date = dt.datetime(
    year=1920,
    month=1,
    day=1
)


def years_ago(years, from_date=None):
    """
    Рандомный рабочий код с StackOverflow
    Учитывает високосный год
    """
    if from_date is None:
        from_date = dt.datetime.now()
    try:
        return from_date.replace(year=from_date.year - years)
    except ValueError:
        # Must be 2/29!
        assert from_date.month == 2 and from_date.day == 29 # can be removed
        return from_date.replace(month=2, day=28,
                                 year=from_date.year-years)


def num_years(begin=foundation_date, end=None) -> int:
    """
    Рандомный рабочий код с StackOverflow
    Учитывает високосный год
    """
    if end is None:
        end = dt.datetime.now()
    years_passed = int((end - begin).days / 365.2425)
    if begin > years_ago(years_passed, end):
        return years_passed - 1
    else:
        return years_passed


def year_form(year: int) -> str:
    f"Функция, которая генерирует правильную форму слова \'год\'"
    if year % 100 == 1:
        return 'год'
    elif (year % 100) in range(2, 5):
        return 'года'
    else:
        return 'лет'

