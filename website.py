from flask import Flask, render_template, request, flash, redirect, url_for, session
from waitress import serve
from form import RegistrationForm, LoginForm
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import threading
import signal
import subprocess
from dotenv import load_dotenv
from db import db, bcrypt, User
import logging
from logging.handlers import RotatingFileHandler

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db.init_app(app)
bcrypt.init_app(app)

with app.app_context():
    db.create_all()

# Set up logging for production
if not app.debug:
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=3)
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)

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
    try:
        name = request.form['name']
        email = request.form['email']
        input_message = request.form['message']
        EMAIL = os.getenv("EMAIL")
        EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
        sender_email = EMAIL
        receiver_email = EMAIL
        password = EMAIL_PASSWORD

        message = MIMEMultipart("alternative")
        message["Subject"] = "Testing python"
        message["From"] = sender_email
        message["To"] = receiver_email

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

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        message.attach(part1)
        message.attach(part2)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return f"Thank you for your message, {name}!"
    except Exception as e:
        app.logger.error(f"Error in submit_contact: {e}")
        return "There was an error processing your request. Please try again later.", 500

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    try:
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('login'))
    except Exception as e:
        app.logger.error(f"Error during registration: {e}")
        flash('An error occurred during registration. Please try again.', 'danger')
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    try:
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                session['user_id'] = user.id  # Store user ID in session
                flash('You have been logged in!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Login unsuccessful. Please check email and password', 'danger')
    except Exception as e:
        app.logger.error(f"Error during login: {e}")
        flash('An error occurred during login. Please try again.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    session.pop('user_id', None)  # Clear user ID from session
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

def open_browser():
    url = "http://127.0.0.1:5000/"
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'  # Adjust the path if needed
    subprocess.Popen([chrome_path, url])

def run_flask_app():
    serve(app, host='127.0.0.1', port=5000)

def signal_handler(sig, frame):
    print('Shutting down gracefully...')
    sys.exit(0)

def notify():
    from win10toast import ToastNotifier

    toast = ToastNotifier()

    toast.show_toast(
        "Reminder",
        "Make sure to ALWAYS have your branches up to date before you start coding! And please work in your VENV at all TIMES! (.venv <tab> scripts <tab> activate) -> to exit: (deactivate)",
        duration=50,
        icon_path="./static/alipic.ico",
        threaded=True,
    )

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database and tables

    signal.signal(signal.SIGINT, signal_handler)

    server_thread = threading.Thread(target=run_flask_app, daemon=True)
    server_thread.start()

    threading.Timer(2, open_browser).start()

    server_thread.join()
