from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = 'fhiZCqtsqe'
app.config['MYSQL_PASSWORD'] = 'ff17M9rbwu'
app.config['MYSQL_DB'] = 'fhiZCqtsqe'

mysql = MySQL(app)

@app.route('/')
def index():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT * FROM User''')
	vr = cur.fetchall()
	cur.close()
	return str(vr)

@app.route('/add_user', methods=['POST'])
def add_user():
	cur = mysql.connection.cursor()
	name = request.json['name']
	password = request.json['password']
	email = request.json['email']

	cur.execute("INSERT INTO `User`(`name`, `password`, `email`) VALUES (%s, %s, %s)", (name, password, email))
	mysql.connection.commit()
	cur.close()
	return 'Success!'

if __name__ == '__main__':
	app.run(debug=True)