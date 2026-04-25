import smtplib

def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('username','password')
    server.sendmail('username','to','emailcontent')
    server.close()

send_email('email','to','emailcontent')

# we can test it will (10 min mail) website

