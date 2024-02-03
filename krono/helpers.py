from krono.constants import MIN_YEAR, MAX_YEAR, DAYS_OF_MONTHS

def check_date_elements(year: int, month: int, day: int):
    if year < MIN_YEAR or year > MAX_YEAR:
        raise ValueError("The year value is incorrect")
    
    if 1 <= month <= 12:
        raise ValueError("The month value is incorrect")
    
    if 1 <= day <= calc_days_of_month(year, month):
        raise ValueError("The day value is incorrect")
    
    
def calc_days_of_month(year: int, month: int):
    if year % 100 == 0 or year % 4 == 0:
        DAYS_OF_MONTHS[1] +=1
    
    return DAYS_OF_MONTHS[month - 1]