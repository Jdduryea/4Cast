"""
Routes and views for the flask application.
"""

"""
Use this command in kudu to update stuff
D:\home\site\wwwroot\env\Scripts>python.exe -m pip install --upgrade -r D:\home\site\wwwroot\requirements.txt 

"""

from datetime import datetime
from flask import render_template, url_for, request
from FlaskWebProject1 import app
import json
import requests
import twilio
import twilio.twiml
from twilio import twiml
#from twilio.rest import TwilioRestClient 


# put your own credentials here 
ACCOUNT_SID = "ACe6dfc70070586ef00b1c5a39c6040522" 
AUTH_TOKEN = "2f49cbdc4d91e523accf22158ca269d2" 

callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+19707655549": "Jack",
}


# Sends a SMS to number with string message as the body
def sendMessage(number, message):
    resp = requests.post("https://api.twilio.com/2010-04-01/Accounts/ACe6dfc70070586ef00b1c5a39c6040522/Messages.json", data={"To":number,"From":"+15107882364","Body":message},auth=("ACe6dfc70070586ef00b1c5a39c6040522","2f49cbdc4d91e523accf22158ca269d2"))


# IT WORKS!!!!!!
@app.route('/sms', methods=['POST'])
def sms():
    # For some reason, the line below is causing an error
    number = request.form['From']
    message_body = request.form['Body']
    resp = twiml.Response()
    resp.message('Hello {}, you said: {}'.format(number, message_body))
    return str(resp)
    #return str(number)

# @app.route("requestPage")
# def get_message():
#     sendMessage("+19707655549","Hey, Jack, I'm trying to reply to you")
#     return "helllloooo"

@app.route('/')
@app.route('/index', methods=["GET","POST"])
def index():
    # This uses the REST API to send an http request
    #resp = requests.post("https://api.twilio.com/2010-04-01/Accounts/ACe6dfc70070586ef00b1c5a39c6040522/Messages.json", data={"To":"+19707655549","From":"+19709646126","Body":"Hi!"},auth=("ACe6dfc70070586ef00b1c5a39c6040522","2f49cbdc4d91e523accf22158ca269d2"))
    
    lat = -1.29
    lon = 36.8
    #resp = requests.post("https://api.twilio.com/2010-04-01/Accounts/ACe6dfc70070586ef00b1c5a39c6040522/Messages.json", data={"To":"+19707655549","From":"+19709646126","Body":"Hi!"},auth=("ACe6dfc70070586ef00b1c5a39c6040522","2f49cbdc4d91e523accf22158ca269d2"))


    # Temp is in Kelvin
    request_str = "http://api.openweathermap.org/data/2.5/forecast?lat="+str(lat)+"&lon="+str(lon)+"&APPID=d619cd297fd19d7934ea3d5dc626b5a7"
    resp = requests.post(request_str)
    data= json.loads(resp.text)
    #   
    city_name = data["city"]["name"]
    print city_name
    msg = "Hey, Jack, you are in " + city_name
    #sendMessage("+19707655549",msg)
   
    

    """Renders the home page."""
    return render_template(
        'index.html'
    )

@app.route('/team')
def team():
    """Renders the contact page."""
    # client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
    # client.messages.create(
    #     to="+19707655549", 
    #     from_="+19709646126", 
    #     body="This is the ship that made the Kessel Run in fourteen parsecs?", 
    #     media_url="https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg", 
    # )
   # sendMessage("+19707655549","Yo what up, Jack?")

    return render_template(
        'team.html'
    )

@app.route('/about', methods=["GET","POST"])
def about():
    """Renders the about page."""
    resp = twiml.Response()
    resp.message("Hi!")

    return render_template(
        'about.html'
        
    )

@app.route('/services')
def services():
    """Renders the about page."""

    return render_template(
        'services.html'
        
    )

if __name__ == "__main__":
    app.run()

# Returns the forecast for a given geographical location expressed in cooridates (latitude and longitude)
# Might also return predictions.
# The output of this function is to be directly sent as the body of an SMS message
def get_forecast(lat, lon):
    """
    Input: the latitude and longitude of a location
    Outout: the weather forecast for that location

    Uses a weather api to return the hourly predicted rain and temperature values for the next few days
    """

    # TODO: Remove these when we are done testing
    lat = -1.29
    lon = 36.8

    # Temp is in Kelvin
    request_str = "http://api.openweathermap.org/data/2.5/forecast?lat="+str(lat)+"&lon="+str(lon)+"&APPID=d619cd297fd19d7934ea3d5dc626b5a7"
    resp = requests.post(request_str)
    data= json.loads(resp.text)
    #   

    rain_dict = {}
    for i in range(0,len(data["list"])):
        if "rain" in data["list"][i]:
            if "3h" in data["list"][i]["rain"]:
                rain_amt = data["list"][i]["rain"]["3h"]
                rain_dict[i] = rain_amt

    temp_dict = {}
    for i in range(0,len(data["list"])):
        temp  = data["list"][i]["main"]["temp"] # temp is in kelvin
        temp = temp - 273.15
        temp_dict[i] = temp

    response = ""
    for val in temp.values():
        response += str(val)
        response += ", "
    return response

