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
    print(userdata)
    airlineClass = userdata["group3"][0]
    city = userdata["group1"][0]
    activities = ""
    # activities = (userdata["group2"][0]) + " " + (userdata["group2"][1]) + " " + (userdata["group2"][2])
    for activity_chosen in userdata["group2"]:
        activities += activity_chosen
        activities += " and "
    # meal = userdata["group4"][0] + " " + (userdata["group4"][1]) +  " " + (userdata["group4"][2])
    meal = ""
    for meal_chosen in userdata["group4"]:
        meal += meal_chosen
        meal += " and "
    hotel = userdata["group5"][0]
    return render_template('results.html', airlineClass=airlineClass, city = city, activities=activities, meal=meal,hotel=hotel)
