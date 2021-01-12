import datetime as dt
import pandas
import random
import smtplib

PLACEHOLDER = "[NAME]"
MY_EMAIL = "dbp.automated.emails@gmail.com"
MY_PASSWORD = "password"

now = dt.datetime.now()
today = (now.month, now.day)
print(today)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    name = birthdays_dict[today]["name"]
    email = birthdays_dict[today]["email"]
    letter = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file=letter) as birthday_letter:
        contents = birthday_letter.read()
        contents = contents.replace(PLACEHOLDER, name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.startlls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=email,
                            msg=f"Subject: Happy Birthday!\n\n{contents}")



