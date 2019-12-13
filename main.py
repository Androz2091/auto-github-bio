# Used to make call to the github API
import requests
# Used to read the config file
import json
# Used to display the last update
from datetime import datetime

# Read the config file
with open("config.json", "r") as f:
    config = json.load(f)


def update_bio(text):
    """
    Update the Github biography of the user
    
    Args:
        text (str): The new biography content

    Returns:
        data (any): The Github response
    """
    url         = "https://api.github.com/user"
    headers     = { "Authorization": "token "+config["github"], "Content-Type" : "text/plain" }
    response    = requests.patch(url, '{ "bio": "'+text+'" }', headers=headers)
    data        = response.json()
    return data


def get_weather_of(city):
    """
    Get the weather of a specific city
    
    Args:
        city (str): The name of the city whose weather we want

    Returns:
        weather (str): The weather of the city
    """
    # Open Weather Map API Base url
    base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+config["weather"]+"&q="+city
    response = requests.get(base_url)
    data     = response.json()
    # Returns weather info (snow, rain, clouds, etc...)
    return data["weather"][0]["main"]


def generate_bio_content(weather):
    """
    Generate the bio content

    Args:
        weather (str): The weather of the city

    Returns:
        bio_content (str): The final bio content
    """
    # The current time (hours and minutes)
    now = datetime.now().strftime("%H:%M")
    # Returns the final string wich contain the city, the weather, the last update and the credits
    return "Current weather in "+config["city"]+": "+weather.upper()+" | Last update: "+now+" | Made by Androz2091 using Python"

def main():
    """
    Main code which call the other functions
    """
    # Get the weather of the city
    weather = get_weather_of(config["city"])
    # Get the bio content
    bio_content = generate_bio_content(weather)
    # Update the biography
    status = update_bio(bio_content)

    # Log
    log_prefix = "["+datetime.now().strftime("%H:%M")+"]"
    # If there is a login attr in the status object, it means the operation is successfull
    if "login" in status:
        print(log_prefix+" Successfully updated biography")
    else:
        # If Github returned a message
        if "message" in status:
            # If the error is caused by the personal access token
            if status["message"] == "Bad credentials":
                print(log_prefix+" Seems like your Github personal access token is invalid...")
            else:
                print(log_prefix+" Something happened. Message is the following: "+status["message"])
        # If Github didn't return anything
        else:
            print(log_prefix+" Something happened. Here is the Github response: "+status["message"])

if(__name__ == "__main__"):
    main()