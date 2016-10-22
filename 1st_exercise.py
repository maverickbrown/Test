import datetime

name = raw_input("What is your name: ")

age = raw_input("How old are you?: ")


i = datetime.datetime.now()
yearBorn = (i.year - int(age)) 
year = (i.year - int(age)) + 100

print "Hello %s, youre current age is %s. You will turn 100 years old in %d" %(name, age, year)
print "You were born in the year: %s " % yearBorn