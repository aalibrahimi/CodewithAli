from flask import Flask, render_template, request
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

# @app.route("/blog")
# def blog():
#     return render_template('blog.html') 

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

if __name__ == '__main__':
    app.run(debug=True)
