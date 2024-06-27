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
    message = request.form['message']
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
