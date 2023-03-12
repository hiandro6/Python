from datetime import date
year = date.today().year
birth = int(input("when was you born?"))
age = year - birth
print(f"the athlete is {age} years old")
if age <= 9:
    c = 'mirim'
elif age <= 14:
    c = "infantil"
elif age <= 19:
    c = "juniôr"
elif age <= 25:
    c = "seniôr"
else:
    c = "master"
print(f"classfication: {c}")
