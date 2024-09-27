from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from form import RegistrationForm, LoginForm
from submit import submit_contact
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configuration
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
# app.config["MAIL_SERVER"] = "smtp.gmail.com"
# app.config["MAIL_PORT"] = 465
# app.config["MAIL_USE_SSL"] = True
# app.config["MAIL_USERNAME"] = os.getenv("EMAIL")
# app.config["MAIL_PASSWORD"] = os.getenv("EMAIL_PASSWORD")

mail = Mail(app)

# Routes
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

# @app.route("/courses")
# def courses():
#     return render_template("courses.html")

# @app.route("/contact")
# def contact():
#     return render_template("contact.html")

@app.route("/submit_contact", methods=["POST"])
def submit():
    submit_contact()
    return redirect(url_for('home'))

# @app.route("/testimonials")
# def testimonials():
#     return render_template("testimonials.html")

# @app.route("/blog")
# def blog():
#     return render_template("blog.html")

# @app.route("/faq")
# def faq():
#     return render_template("faq.html")


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5001)