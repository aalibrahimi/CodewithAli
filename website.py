import subprocess
from flask import Flask, render_template, request
import threading

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
    message = request.form['message']
    # Here you would typically process the contact form submission
    # For example, save it to a database or send an email
    return f"Thank you for your message, {name}!"

def open_browser():
    url = "http://127.0.0.1:5000/"
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'  # Adjust the path if needed
    subprocess.Popen([chrome_path, url])

if __name__ == '__main__':
    # Run the browser in a separate thread to avoid blocking
    threading.Timer(1, open_browser).start()
    # Start Flask app
    app.run(debug=True)
