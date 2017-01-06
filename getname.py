from getday import DayName 
import json
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument("-y",help="the year in which you were born",type=int,required=True)
parser.add_argument("-d",help="the day on which you were born",type=int,required=True)
parser.add_argument("-m",help="the month in which you were born",type=int,required=True)
args = parser.parse_args()
print args

yryr = args.y
yrmo = args.m
yrdy = args.d
yrbirthday = DayName(yryr,yrmo,yrdy)

#get the day of the week on which the person was born from the Dayname class (determined when the function is initiated) 
xday = yrbirthday.dayofbirth; 

#run a method from the DayName class, depending on the day of the week on which the person was born
getattr(yrbirthday,xday)()
 
response = {'Date of birth':yrbirthday.readabledate,'Day of birth':yrbirthday.dayofbirth,'Male names':yrbirthday.male,'Female names':yrbirthday.female}

print "Content-type: application/json"
print(json.JSONEncoder().encode(response))
