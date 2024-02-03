from krono.helpers import check_date_elements

class Date:
    _DEFAULT_PATTERN="%Y-%m-%d"
    _DELIMITERS = ["-", "/", ":", " "]
    
    def __new__(cls, year: int, month: int, day: int):
        check_date_elements(year, month, day)
        
        self = object.__new__(cls)
        self._year = year
        self._month = month
        self._day = day
        
        return self
    
    
    def _convert_to_string(self, pattern: str) -> str:
        specs = {
            "full_year": "{:04d}",
            "month": "{:02d}",
            "day": "{:02d}"
        }
        
        return pattern.replace("%Y", specs["full_year"].format(self._year)) \
            .replace("%m", specs["month"].format(self._month)) \
            .replace("%d", specs["day"].format(self._day))
        
    def __str__(self):
        return self._convert_to_string(self._DEFAULT_PATTERN)