#To get changes do: git pull (for all branches)

from flask import Flask, render_template
app = Flask(__name__)

#Stacking @app.route() will make it so the user can enter in the URL bar any name (that we wrote) and it'll take them to the same (part of the) website.
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

#Putting @app.route() seperate will make a new 'tab' on the website.
@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)