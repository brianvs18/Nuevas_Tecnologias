from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def start():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/singin')
def singin():
    return render_template('singin.html')

@app.route('/singup')
def singup():
    return render_template('singup.html')

if __name__ == "__main__":
    app.run(debug=True)