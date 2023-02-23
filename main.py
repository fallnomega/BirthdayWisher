import random
import smtplib
import datetime as dt
#smtp.gmail.com
# Below are steps specific to users sending email from Gmail addresses.
# 2. Make sure you've enabled less secure apps if you are sending from a Gmail account. (Refer to the video in the next lesson for steps).
# 3. Try to go through the Gmail Captcha here while logged in to the Gmail account: https://accounts.google.com/DisplayUnlockCaptcha
# 4. Add a port number by changing your code to this:
# smtplib.SMTP("smtp.gmail.com", port=587)


# get quotes from quotes.txt and pick a random from it
with open("quotes.txt", 'r',newline='\n') as file:
    quotes = file.readlines()
    file.close()
quote = random.choice(quotes)

today_is = dt.datetime.now()
if today_is.weekday()==0:
    email = "YOUR_EMAIL_HERE"
    password = "YOUR_PASSWORD"
    connection = smtplib.SMTP("SMTP.SERVER.COM","PORT")
    connection.ehlo()
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(from_addr=email,
                        to_addrs="TO_EMAIL",
                        msg=f"Subject:Testing\n\nHello, is it me you're looking for?\n\n{quote}")
    connection.close()

