from flask import Flask, session

app = Flask(__name__)
app.secret_key='dfhkjhndfsglbvhkjdsh1237846y4ehndfvbjhafsvdh'

@app.route('/setuser/<user>')
def setuser(user: str) -> str:
	session['user'] = user
	return 'User value set to: ' + session['user']

@app.route('/getuser')
def getuser() -> str:
	return 'User value is currently set to: ' + session['user']

if __name__ == '__main__':
	app.run(debug=True)