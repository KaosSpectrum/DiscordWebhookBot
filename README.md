Perforce commit webhook bot.

(C)2019 KaosSpectrum

Installation:
1. Open app.py and edit the 3 variables at the top of the file.
  LoginUser, LoginPassword, WebhookURL

2. run  pip install -r requirements.txt to install required dependencies.

3. Launch bot via python app.py&

Bot will launch and get the last submitted change from discord. This should work for
all types of authentication, including tickets.
