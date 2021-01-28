from flask import Flask
from flask import render_template, request
app = Flask(__name__)

@app.route('/DSSHome', methods=['GET'])
def index():
	return render_template('index.html')
	
@app.route('/Doc', methods=['GET'])
def Doc():
	return render_template('DOCMAN.html')
	
@app.route('/Sign', methods=['GET'])
def Sign():
	return render_template('DocSign.html')
