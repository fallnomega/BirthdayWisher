import random
import smtplib
import datetime as dt
import pandas as pd

# smtp.gmail.com
# Below are steps specific to users sending email from Gmail addresses.
# 2. Make sure you've enabled less secure apps if you are sending from a Gmail account. (Refer to the video in the next lesson for steps).
# 3. Try to go through the Gmail Captcha here while logged in to the Gmail account: https://accounts.google.com/DisplayUnlockCaptcha
# 4. Add a port number by changing your code to this:
# smtplib.SMTP("smtp.gmail.com", port=587)


# get quotes from quotes.txt and pick a random from it
with open("quotes.txt", 'r', newline='\n') as file:
    quotes = file.readlines()
    file.close()
quote = random.choice(quotes)

# get birthday info from birthdays.csv
birthdays = pd.read_csv("birthdays.csv")
todays_date = dt.datetime.now()
for x in range(len(birthdays)):
    b_name = birthdays.iloc[x, 0]
    b_email = birthdays.iloc[x, 1]
    b_year = birthdays.iloc[x, 2]
    b_month = birthdays.iloc[x, 3] = birthdays.iloc[x, 3]
    b_day = birthdays.iloc[x, 4]
    age = todays_date.year - b_year

    # pick letter template to use
    letter_number = random.randint(1, 3)
    lettername = f"letter_{letter_number}.txt"
    letter_to_send = ''
    with open(lettername, 'r') as letter_selected:
        letter_to_send = letter_selected.read()
        letter_selected.close()
    letter_to_send = letter_to_send.replace('[NAME]', b_name)
    # send birthday email if today is someone's birthday
    if todays_date.month == b_month and todays_date.day == b_day:
        email = "YOUR EMAIL ADDRESS"
        password = "YOUR EMAIL PASSWORD"  # NOT SECURE BUT FOR LEARNING EXERCISE WE SHALL STORE IT HERE
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.ehlo()
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=f"{b_email}",
                            msg=f"Subject:Happy {age} Birthday {b_name}!\n\n{letter_to_send}\n\nP.S. Here is an inspirational Quote for you: {quote}")
        connection.close()
