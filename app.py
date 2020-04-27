import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/scraper', methods=['GET','POST'])
def scraper():
    session = subprocess.Popen(['./runScraper.sh'], stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = session.communicate()
    if stderr:
        raise Exception("Error "+str(stderr))
    return stdout.decode('utf-8')


@app.route('/email-them', methods=['GET','POST'])
def emailer():
    session = subprocess.Popen(['./runEmailer.sh'])

@app.route("/")                   
def home():      
    return render_template("index.html")
@app.route("/potential")
def potential():
    return render_template("data.html")
@app.route("/confirmed")
def confirmed():
    return render_template("confirmed.html")
@app.route("/404")
def _404():
    return render_template("404.html")
@app.route("/blank")
def blank():
    return render_template("blank.html")
@app.route("/buttons")
def buttons():
    return render_template("buttons.html")
@app.route("/cards")
def cards():
    return render_template("cards.html")
@app.route("/anim-utils")
def animutils():
    return render_template("utilities-animation.html")
@app.route("/bord-utils")
def bordutils():
    return render_template("utilities-border.html")
@app.route("/colr-utils")
def colrutils():
    return render_template("utilities-color.html")
@app.route("/othr-utils")
def othrutils():
    return render_template("utilities-other.html")


if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app