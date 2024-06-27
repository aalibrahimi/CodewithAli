import subprocess
import threading
import signal
import sys
from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/courses")
def courses():
    return render_template('courses.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/testimonials")
def testimonials():
    return render_template('testimonials.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/faq")
def faq():
    return render_template('faq.html')

@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    input_message = request.form['message']
    import smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    import os
    from dotenv import load_dotenv
    load_dotenv()
    EMAIL=os.getenv("EMAIL")
    EMAIL_PASSWORD=os.getenv("EMAIL_PASSWORD")
    sender_email = EMAIL
    receiver_email = EMAIL
    password = EMAIL_PASSWORD

    message = MIMEMultipart("alternative")
    message["Subject"] = "Testing python"
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
    return f"Thank you for your message, {name}!"

def open_browser():
    url = "http://127.0.0.1:5000/"
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'  # Adjust the path if needed
    subprocess.Popen([chrome_path, url])

def run_flask_app():
    serve(app, host='127.0.0.1', port=5000)

def signal_handler(sig, frame):
    print('Shutting down gracefully...')
    sys.exit(0)

if __name__ == '__main__':
    # Register the signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    
    # Start the Flask server in a new thread and ensure it stays alive
    server_thread = threading.Thread(target=run_flask_app, daemon=True)
    server_thread.start()
    
    # Open the browser after a short delay
    threading.Timer(2, open_browser).start()
    
    # Keep the main thread alive to let the server thread run
    server_thread.join()
