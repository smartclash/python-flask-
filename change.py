from flask import Flask, render_template
app = Flask(__name__)

@app.route("/hello")
def hello():
    headline = "Hello world"
    return render_template("change.html" , headline = headline)

@app.route("/")
def bye():
    headline = "Goodbye" 
    return render_template("change.html" , headline = headline)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
