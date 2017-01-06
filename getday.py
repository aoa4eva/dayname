import sys
import datetime 

class DayName: 
    def Monday(self):
        # Sets values for Monday (male and female). Equivalent functions do the same for all the other days of the week.
        # These can be put into a database later and managed for various tribes
        self.male=['Kwadwo']
        self.female=['Adwoa']
    def Tuesday(self):
        self.male=['Kwabena']
        self.female=['Abena']
    def Wednesday(self):
        self.male=['Kweku']
        self.female=['Akua']
    def Thursday(self):     
        self.male=['Yaw']
        self.female=['Yaa']
    def Friday(self):     
        self.male=['Kofi']
        self.female=['Afua']
    def Saturday(self):     
        self.male=['Kwame']
        self.female=['Ama']
    def Sunday(self):     
        self.male=['Kwesi']
        self.female=['Akosua']

    def __init__(self,yryear,yrmonth,yrday):
        # Defines class values for broken down parts of the date of birth (year, month, day)
        # Also indicates the day of birth and a readable date (day of the week, day, month, year) 
        self.yrday=yrday 
        self.yrmonth=yrmonth
        self.yryear=yryear     
        self.birthdate = datetime.date(self.yryear,self.yrmonth,self.yrday)
        self.dayofbirth = self.birthdate.strftime("%A")
        self.readabledate= self.birthdate.strftime("%A %d %B %Y")