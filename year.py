import datetime
from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello():
   now = datetime.datetime.now()
   new_year = now.month == 1 and now.day == 1
   new_year = True
   return render_template("newyear.html" ,new_year = new_year)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)