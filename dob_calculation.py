# import random and time module
import random
import time

# greets for user
greet = ['Hai', 'Hello', 'Hi', 'Hey']
# get details from user
name = input("What's your name? ")
print(random.choice(greet), "" + name, "Let's calculate your 'age'")
time.sleep(0.5)
birth_date = int(input("Enter your birth date: "))
time.sleep(0.5)
birth_month = int(input("Enter your birth month(in number): "))
time.sleep(0.5)
birth_year = int(input("Enter your birth year: "))
time.sleep(0.5)
# current date, month, year defined for calculation
current_date = 26
current_month = 4
current_year = 2020
age_days = []
age_months = []
age_years = []
# if condition for if birth date if more than current date
if birth_date > current_date:
    current_date = current_date + 30
    current_month = current_month - 1
    age_days = current_date - birth_date
    # nested if condition for if birth month is higher than current month
    if birth_month > current_month:
        current_month = current_month + 12
        current_year = current_year - 1
        age_months = current_month - birth_month
    else:
        age_months = current_month - birth_month
else:
    age_days = current_date - birth_date
    # if condition for if birth month is more than current month
    if birth_month > current_month:
        current_month = current_month + 12
        current_year = current_year - 1
        age_months = current_month - birth_month
    else:
        age_months = current_month - birth_month
age_years = current_year - birth_year

print("You are ", age_years,"years ", age_months, "months ", age_days, "days right now")
