from flask import Flask, render_template, request, redirect, url_for
import mysql.connector 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="taskapp"
)
app = Flask(__name__)

@app.route('/')
def index():
    sql = "SELECT * FROM example"
    cur = mydb.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    print(result)
    return render_template('home.html', example = result)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/createtask')
def createtask():
    return render_template('create-task.html')

@app.route('/addtask', methods=['POST'])
def addtask():
    if request.method == 'POST':
        taskName = request.form['taskName']
        taskDate = request.form['taskDate']
        print("taskName", taskName, " taskDate", taskDate)
        cur = mydb.cursor()
        sql = f"INSERT INTO example (task,date) VALUES ('{taskName}','{taskDate}')"
        cur.execute(sql)
        mydb.commit()
        return redirect(url_for('index'))
    return "Error"

if __name__ == "__main__":
    app.run(debug=True)