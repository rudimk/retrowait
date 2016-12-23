from __future__ import division
import arrow
import wikipedia
import math

class Wait:
    progress = None
    current_date = arrow.now()
    back_date = None
    progress_in_years = None
    year = None

    def __init__(self, progress):
        self.progress = progress/100
        self.progress_in_years = math.exp(20.344*(self.progress**3)+3) - math.exp(3)
        self.back_date = self.current_date.replace(years=-int(self.progress_in_years))
        self.year = self.back_date.year
    
    def info(self):
        print wikipedia.summary(str(self.year))
        


