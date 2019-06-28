from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/italy')
def italy():
    return render_template('italy.html')
    
@app.route('/USA')
def USA():
    return render_template('USA.html')
    
@app.route('/france')
def france():
    return render_template('france.html')
    
@app.route('/australia')
def australia():
    return render_template('australia.html')
    
@app.route('/china')
def china():
    return render_template('china.html')
    
@app.route('/bahamas')
def bahamas():
    return render_template('bahamas.html')
    
@app.route('/results', methods = ["POST", "GET"])
def results():
    userdata = dict(request.form)
    airlineClass = userdata['group3'][0]
    print(airlineClass)
    return render_template('results.html', airlineClass=airlineClass)
