from flask import Flask, render_template, request, redirect
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'aSecret'
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'friends')
# an example of running a query
# print mysql.query_db("SELECT * FROM friendList")

@app.route('/')
def mainpage():
    # temp = 'nihao'
    # return render_template('index.html', tempp = "yoyoo")
    query = "SELECT * FROM friendList"
    friends = mysql.query_db(query)
    forHTML = friends
    print forHTML
    return render_template('index.html', tempp=forHTML)

@app.route('/add', methods=['POST'])
def submitted():
    data = {
        'name': request.form['name'],
        'age': request.form['age']
    }

    query = 'INSERT INTO `friends`.`friendList` (`name`, `age`, `since`) VALUES (:name, :age, NOW());'
    friends = mysql.query_db(query, data)
    print friends
    return redirect('/')

app.run(debug=True)