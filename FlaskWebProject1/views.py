"""
Routes and views for the flask application.
"""

"""
Use this command in kudu to update stuff
D:\home\site\wwwroot\env\Scripts>python.exe -m pip install --upgrade -r D:\home\site\wwwroot\requirements.txt 

"""

from datetime import datetime
from flask import render_template, url_for
from FlaskWebProject1 import app
#import requests
import twilio
#from twilio.rest import TwilioRestClient 

# put your own credentials here 
ACCOUNT_SID = "ACe6dfc70070586ef00b1c5a39c6040522" 
AUTH_TOKEN = "2f49cbdc4d91e523accf22158ca269d2" 


# Sends a SMS to number with string message as the body
def sendMessage(number, message):
    resp = requests.post("https://api.twilio.com/2010-04-01/Accounts/ACe6dfc70070586ef00b1c5a39c6040522/Messages.json", data={"To":number,"From":"+19709646126","Body":message},auth=("ACe6dfc70070586ef00b1c5a39c6040522","2f49cbdc4d91e523accf22158ca269d2"))



# @app.route("requestPage")
# def get_message():
#     sendMessage("+19707655549","Hey, Jack, I'm trying to reply to you")
#     return "helllloooo"

@app.route('/')
@app.route('/index', methods=["GET","POST"])
def index():
    # This uses the REST API to send an http request
    #resp = requests.post("https://api.twilio.com/2010-04-01/Accounts/ACe6dfc70070586ef00b1c5a39c6040522/Messages.json", data={"To":"+19707655549","From":"+19709646126","Body":"Hi!"},auth=("ACe6dfc70070586ef00b1c5a39c6040522","2f49cbdc4d91e523accf22158ca269d2"))
   # sendMessage("+19707655549","Hey Jack")
   
    
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

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html'
        
    )

@app.route('/services')
def services():
    """Renders the about page."""
    return render_template(
        'services.html'
        
    )


# Custom "API" wrapper for twilio http requests


