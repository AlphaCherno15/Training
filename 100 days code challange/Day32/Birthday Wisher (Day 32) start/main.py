import smtplib, datetime as dt, random as rd, pandas as pd
# ---------------------------- day management ------------------------------- #
now = dt.datetime.now()
today_month = now.month
today_is = now.day
today_is_what = now.weekday

# ---------------------------- sorting quotes------------------------------- #
def quote():
    with open("quotes.txt", "r") as data:
        # data.readlines() works better
        phrases = data.read().split('\n')
        phrase = rd.choice(phrases)
        return phrase
# ---------------------------- Birthday send------------------------------- #
def b_day():
    data = pd.read_csv("birthdays.csv")
    data_dict = data.to_dict('records')
    for each in data_dict:
        day = int(each['day'])
        month = int(each['month'])
        if today_month == month and today_is == day:
            person = each['name']
            email_send= each['email']
            message = pick_letter(person)
            send(message, email_send, "Happy Birthday")
# ---------------------------- pick a letter for birthday------------------------------- #
def pick_letter(name):
    num = rd.randint(1, 3)
    with open(f"letter_templates/letter_{num}.txt", "r") as data:
        letter = data.read().replace("[NAME]", name)
    return letter
# ---------------------------- send email ------------------------------- #
my_email = "xxxxxxx@gmail.com"
password = "xxxx"

def send(text, email_to_send, subject):
    print(
        f'to: {email_to_send}\n\n'
        f'Subject: {subject}\n\n'
        f'{text}'
    )
    # with smtplib.SMTP("smtb.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=my_email, password=password)
    #     connection.sendmail(from_addr=my_email, to_addrs=email_to_send, msg=f'Subject: {subject} Birthday\n\n{text}')
b_day()

