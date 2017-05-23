# Dayname
Get the Akan male and female day names from the date of birth entered

This is a python script to determine the male and female names of a person whose date of birth is entered in a python prompt. 
The script takes the following parameters (all of which are required, but do not have to be entered in a particular order): 

1. -d : The day on which the person was born. This can be with or without the leading zero 

2. -m: The month in which the person was born. This can be with or without the leading zero 

3. -y: The year in which the person was born. 4 digits suggested. 

Thanks [@atwumb](http://www.github.com/atwumb) for the idea and inspiration. 

To use this, ensure you have Python 2.7 installed (I haven't checked for compatibility with 3)

How to use this script: 

1. Copy the files to the directory 

2. Run the script, using the example below

python getname.py -m6 -d2 -y2015

This will return a JSON result in this format: 

{"Date of birth": "Tuesday 02 June 2015", "Female names": ["Abena"], "Male names": ["Kwabena"], "Day of birth": "Tuesday"}

The script can easily be modified to return more than one name per gender per day, since there may be variations of each a name. 
