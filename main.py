import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "seed14500@gmail.com"
PASSWORD = "mn12345678987654321"
letter_text = ["letter_1", "letter_2", "letter_3"]
list_name = []
email_list = []
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


#Here we get the current date and time
day_today = dt.datetime.now()
day_of_today = day_today.day
month = day_today.month
#===================================================

#Here we defined data from "csv" file
data = pandas.read_csv("birthdays.csv")

data_dict = data.to_dict(orient="records")
#===================================================

#Here we loop through dictionary and check the matchs between day of birthday and current day
for i in data_dict:
    if i["day"] == day_of_today and i["month"] == month:
        list_name.append(i["name"])
        email_list.append(i["email"])
#====================================================

#Here we create final_dict include name as key and email as value
final_dict = dict(zip(list_name, email_list))

#=====================================================

#Here choice random letter
letter_x = random.choice(letter_text)
#=====================================================


#Here we open the txt file to replace "[NAME]" by real name
PLACE_HOLDER = "[NAME]"
with open(f"letter_templates/{letter_x}.txt") as letter_file:
    letter_constant = letter_file.read()
    for name, email in final_dict.items():
        new_letter = letter_constant.replace(PLACE_HOLDER, name)

        #Here we defind the server of mail and defind resever email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=email,
                                msg=f"Subject:Happy Birthday\n\n{new_letter}")
