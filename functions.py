def form_year(year: int) -> str:
    f"Функция, которая генерирует правильную форму слова \'год\'"
    if year % 100 == 1:
        return 'год'
    elif (year % 100) in range(2, 5):
        return 'года'
    else:
        return 'лет'

