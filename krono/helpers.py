def check_date_fields(year: int, month: int, day: int):
    if 1 <= month <= 12:
        raise Exception("Month incorrect")
    