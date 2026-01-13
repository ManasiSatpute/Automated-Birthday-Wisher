#  Automated Birthday Wisher (Python)

This is a Python mini project that automatically sends personalized birthday wishes via email.  
It checks a CSV file for birthdays matching today’s date and sends a customized email using a randomly selected template.

---

##  Features

- Automatically checks birthdays using date matching
- Sends personalized birthday emails
- Uses multiple email templates randomly
- Secure email sending via SMTP
- Beginner-friendly Python project

---

##  Technologies Used

- Python
- pandas
- smtplib
- datetime
- random


---

##  Project Structure
```
automated-birthday-wisher/
│
├── birthdays.csv
├── main.py
├── letter_templates/
│ ├── letter_1.txt
│ ├── letter_2.txt
│ └── letter_3.txt
└── README.md
```
---

##  Sample `birthdays.csv`

```csv
name,email,year,month,day
Manasi,example@gmail.com,2003,1,13
```
##  Sample `letter.txt`
```

Dear [NAME],

It's your birthday! Have a great day!

Best wishes,
Angela

```







