import pandas
import smtplib
import datetime as dt
import random

my_email = "your_email@gmail.com"
password = "your_app_password"

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")

new_dict = {
    (row["month"], row["day"]): row
    for (_, row) in data.iterrows()
}

if today in new_dict:
    birthday_person = new_dict[today]

    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path, encoding="utf-8") as file:
        content = file.read()

    
    content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Birthday Wish!\n\n{content}"
        )
