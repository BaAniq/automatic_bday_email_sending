import datetime as dt
import pandas
import random
import smtplib
my_email = "dimitoret@gmail.com"
my_password = "jonq cuqh zjgt trqe "

today = dt.datetime.now()
day_today = today.day
month_today = today.month

birthday_data = pandas.read_csv("birthdays.csv")

for (index, row) in birthday_data.iterrows():

    if row.month == month_today and row.day == day_today:
        num_letter = random.choice(range(1, 4))
        with open(f'letter_templates/letter_{num_letter}.txt') as letter:

            letter_str = letter.read()
            letter_str = letter_str.replace('[NAME]', row.first_name)
            with open(f'email_to_{row.first_name}', 'w+') as new_letter:
                new_letter.write(letter_str)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=row.email, msg=f'Subject:Happy Birthday!\n\n{letter_str}')



