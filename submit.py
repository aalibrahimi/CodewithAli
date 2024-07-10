import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import request, flash
import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()



def submit_contact():
    name = request.form['name']
    email = request.form['email']
    input_message = request.form['message']
    EMAIL=os.getenv("EMAIL")
    EMAIL_PASSWORD=os.getenv("EMAIL_PASSWORD")
    sender_email = EMAIL
    receiver_email = EMAIL
    password = EMAIL_PASSWORD

    message = MIMEMultipart("alternative")
    message["Subject"] = "CodeWithAli Contact Form"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    html = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }}
        .container {{
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}
        .header {{
            background-color: #4CAF50;
            color: white;
            padding: 10px 0;
            text-align: center;
            border-radius: 5px 5px 0 0;
        }}
        .body {{
            padding: 20px;
            line-height: 1.6;
        }}
        .footer {{
            background-color: #f1f1f1;
            color: #555555;
            text-align: center;
            padding: 10px;
            border-radius: 0 0 5px 5px;
            font-size: 12px;
        }}
        .button {{
            display: inline-block;
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            border-radius: 5px;
            margin: 20px 0;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Email Header</h1>
        </div>
        <div class="body">
            <p>From {name} ({email}),</p>
            <p>{input_message}</p>
            <a href="#" class="button">Call to Action</a>
            <p>Thank you!</p>
            <p>Best regards,</p>
            <p>CodeWithAli</p>
        </div>
        <div class="footer">
            <p>&copy; 2024 CodeWithAli. All rights reserved.</p>
            <p><a href="#">Unsubscribe</a></p>
        </div>
    </div>
</body>
</html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    return flash(f"Thank you for your message, {name}!")
