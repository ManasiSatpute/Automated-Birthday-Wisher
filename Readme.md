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


Currently, the script runs manually. To automatically send birthday emails every day, you can deploy it to a cloud platform and schedule it:

### Using PythonAnywhere

1. **Sign up** at [PythonAnywhere](https://www.pythonanywhere.com/).
2. **Upload your project**:
   - Upload `main.py`, `birthdays.csv`, and `letter_templates/` folder.
3. **Set environment variables** for your email and app password:
   - Go to the **"Web"** or **"Files"** section and set `EMAIL` and `PASSWORD`.
4. **Create a scheduled task**:
   - Go to the **Tasks** tab → Add a new scheduled task.
   - Enter the command:  
     ```bash
     python3 /home/yourusername/automated-birthday-wisher/main.py
     ```
   - Set the schedule to **daily at a specific time** (e.g., 9:00 AM).
5. **Save** the task. The script will now run automatically every day.







