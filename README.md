# Automatized Github Biography

📚 Automatized Github biography using openweathermap.org API

Remember to 🌟 this Github if you 💖 it.

![a1](https://i.imgur.com/RGvPQjt.png)

## Installation

### [Github] Create your personal access token

You have to create a **personal access token**, to allow your app to update your biography. Click [here](https://github.com/settings/tokens/new) to go to the personal access token creation page. Select the `User` field (Update all user data) and click `Generate new token`. Copy and paste it in your **config.json** file (`github` field).

### [OpenWeatherMap] Get your application key

You have to get your **openweathermap.org api key**, to allow your app to get the weather of your favourite city. Register [here](https://openweathermap.org/home/sign_up), then go on [your dashboard](https://home.openweathermap.org/api_keys) to get your key. Copy and paste it in your **config.json** file (`weather` field).

### [Crontab] Run the script every 5 minutes

You have to edit the **crontab table** using `crontab -e`. Then, add the following line to this file:  
```sh
*/5 * * * * cd /path/to/auto-github-bio && /usr/bin/python3 /path/to/auto-github-bio/main.py >> ~/cron.log 2>&1
```
This will run the script and update your biography every 5 minutes.

### That's it

Congratulations, you have successfully installed Automatized Github Biography. Feel free to open an issue if necessary!

### Support me on patreon

Thanks to **[LeonardSSH](https://github.com/LeonardSSH)** for their contributions!

Feel free to support me on Patreon so that I can continue to finance my open source projects! Thanks!  

<a href="https://www.patreon.com/bePatron?u=20304709"><img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png"></a>
