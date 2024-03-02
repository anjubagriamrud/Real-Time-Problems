def ageCalculator(a, b, c):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(a, b, c)
    age = int((today-dob).days / 365.25)
    print(age)
#ageCalculator(2002, 9, 1)
y=int(input("Enter year: "))
m=int(input("Enter month: "))
d=int(input("Enter day: "))
ageCalculator(y, m, d)
