#To get changes do: git pull (for all branches)

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/ali")
def blazehp():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)