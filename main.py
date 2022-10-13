import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

_ = load_dotenv()


# From https://mljar.com/blog/python-send-email/
def send_email(to, subject, message, alt_html):
    try:
        email_address = os.environ.get("EMAIL_ADDRESS")
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
        part2 = MIMEText(alt_html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)

        # send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
        return True
    except Exception as e:
        print("Problem during send email")
        print(str(e))
    return False


send_email("mark86v@gmail.com", "Test", "Hello world!", """\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="en">
<head>
    <title>Title</title>
    <meta name="format-detection" content="date=no">
    <meta name="format-detection" content="telephone=no">
    <meta content="width=device-width, initial-scale=1" name="viewport"/>
    <style type="text/CSS"></style>
</head>
<body>
<h1>Test Email</h1>
<p>Hello world!</p>
</body>
</html>""")
