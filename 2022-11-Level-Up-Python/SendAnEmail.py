"""
Challenge:      Write a Python function to send a basic email notification

Input:          Reciever email
                Address
                Subject Line
                Message Body


"""




##### ##### ##### ##### ##### Instructor's Solution

import smtplib

SENDER_EMAIL = 'example@example.com'
SENDER_PW = 'Example'

def send_email(receiver_email, subject, body):
    message = f'Subject {subject}\n\n{body}'
    with smtplib.SMTP('smtp.office365.com', 587) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PW)
        server.sendmail(SENDER_EMAIL, receiver_email, message)