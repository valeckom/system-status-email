# From https://mljar.com/blog/python-send-email/
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(to, subject, message, message_html):
    email_address = os.environ.get("EMAIL_FROM_ADDRESS")
    email_password = os.environ.get("EMAIL_PASSWORD")

    if email_address is None or email_password is None:
        # no email address or password
        # something is not configured properly
        print("Did you set email address and password correctly?")
        return False

    # create email
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = to

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(message, 'plain')
    part2 = MIMEText(message_html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)

        if os.environ.get('dry_run'):
            return

        smtp.send_message(msg)
