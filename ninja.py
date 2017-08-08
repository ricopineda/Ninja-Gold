from flask import Flask, render_template, request, redirect, session

import random
app = Flask(__name__)
app.secret_key = 'mySecret'

@app.route('/')

def index():
	
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])                           
                                        
def gold_count():


	if request.form['building'] == 'farm':
		session['counter'] += int(random.randrange(10, 20))
	elif request.form['building'] == 'cave':
		session['counter'] += int(random.randrange(5,10))
	elif request.form['building'] == 'house':
		session['counter'] += int(random.randrange(2,5))
	elif request.form['building'] == 'casino':
		session['counter'] += int(random.randrange(-50, 50))
	
	print request.form
	print session


	return redirect('/')

@app.route('/process', methods=['POST']) 

def reset():
	session['counter'] = 0
	print session


	return render_template('index.html')

app.run(debug=True)