# Automatized Github Biography

📚Automatized Github biography using openweathermap.org API

## Installation

### [Github] Create your personal access token

You have to create a **personal access token**, to allow your app to update your biography. Click [here](https://github.com/settings/tokens/new) to go to the personal access token creation page. Select the `User` field (Update all user data) and click `Generate new token`. Copy it and keep it somewhere.

### [OpenWeatherMap] Get your application key

You have to get your **openweathermap.org api key**, to allow your app to get the weather of your favourite city. Register [here](https://openweathermap.org/home/sign_up), then go on [your dashboard](https://home.openweathermap.org/api_keys) to get your key. Copy it and keep it somewhere.

### [Github Secrets] Add some secrets

* `GITHUB_TOKEN` the **personal access token** you just created above.
* `WEATHER_TOKEN` the **openweathermap.org api key** you just created above.
* `CITY_NAME` the **name of the city** you want to take the weather from. (it must be valid, you can check it: https://openweathermap.org/)
* `TEMP_UNITS` the **unit of measurement** in which you want the temperature to be displayed. (the available ones can be found here: https://openweathermap.org/current#data)

### Run the script every 5 minutes using Github Actions

- To see a real example, visit [here](https://github.com/unthreaded/git-hooks/blob/92ea6bde348431fbe25d05c33398c969eec5d3ee/.github/workflows/build.yml#L48).
```yaml
   - name: Setup Python
     uses: actions/setup-python@v2
     with:
       python-version: 3.8 
   - name: Execute py script
     if: always()
     env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        WEATHER_TOKEN: ${{ secrets.WEATHER_TOKEN }}
        CITY_NAME: ${{ secrets.CITY_NAME }}
        TEMP_UNITS: ${{ secrets.TEMP_UNITS }}
     run: |
       git clone https://github.com/LeonardSSH/auto-github-bio.git auto-github-bio
       python auto-github-bio/main.py $GITHUB_TOKEN $WEATHER_TOKEN $CITY_NAME $TEMP_UNITS
```

This will run the script and update your biography every 5 minutes.

### That's it

Congratulations, you have successfully installed Automatized Github Biography. Feel free to open an issue if necessary!

### Support me on patreon

Feel free to support me on Patreon so that I can continue to finance my open source projects! Thanks!  

<a href="https://www.patreon.com/bePatron?u=20304709"><img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png"></a>
