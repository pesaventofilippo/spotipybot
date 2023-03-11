# DISCLAIMER - PLEASE READ BEFORE USING
This project was a proof of concept and was written years ago. **It doesn't work anymore**, as Spotify's website changed.  
You're free to fork this repo and update it if you want, but please **do not message or ask me for help** about writing an updated version.  
Automating "fake" interactions is against Spotify's ToS and I don't want nor have the time to be involved with this project anymore.


# SpotiPyBot
A Python-written bot that can generate automatic listens to a given playlist.\
It now supports multi-account, multithreading and headless Chrome!

## Usage
* First, clone this repo on your local machine with\
```$ git clone https://github.com/pesaventofilippo/spotifybot.git```

* Then, download the right **chromedriver** for your Chrome version from [here](http://chromedriver.chromium.org/downloads) and put it under the ```drivers``` subfolder

* Create a list of Spotify profiles for this program to use and write it in ```data/profiles.json```.\
Example:\
```{```\
```    "credentials": [```\
```        {"username": "firstprofile@example.com",```\
```            "password": "first_password"},```\
```        {"username": "secondprofile@example.com",```\
```            "password": "second_password"}```\
```        {"username": "thirdprofile@example.com",```\
```            "password": "third_password"}```\
```    ]```\
```}```

* Done! You can now simply run the bot with\
```$ python3.6 main.py [options]```

## Run options
These are optionals parameters, they are not mandatory to run the program.

* ```--headless``` puts Chrome in headless mode, useful if you do not have a DE
