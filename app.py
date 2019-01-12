import os
import subprocess
import time
from datetime import datetime
from discord_webhooks import DiscordWebhooks
from P4 import P4

Username = "YourUsername"
Password = "YourPassword"
WebhookURL = "YourWebhookURL"

change_list = {
  'lastchange': ''
}

def connect():
 p4.user = Username
 p4.password = Password
 p4.connect()
 p4.run_login()

def get_changes():
  p4_changes = p4.run_changes("-t", "-m 1", "-l")

  if not p4_changes[0]:
   return ''

  ts = int(p4_changes[0].get("time"))
  time = datetime.utcfromtimestamp(ts).strftime('%d/%m/%Y %H:%M:%S')
  change = p4_changes[0].get("change")
  user =  p4_changes[0].get("user")
  client = p4_changes[0].get("client")
  desc =  p4_changes[0].get("desc")

  output = "Change " + change + " on " + time + " by " + user + "@" + client + "\n\n" + desc

  if output != change_list['lastchange']:
    change_list['lastchange'] = output

    if '*pending*' in output:
      return ''

    else:
      return output

  else:
    return ''

def post():
  discord_text = get_changes()

  if discord_text != '':
    message = DiscordWebhooks(WebhookURL)
    message.set_content(color=0xc8702a, description='`%s`' % (discord_text))
    message.set_author(name='Perforce Changelist Submit')
    message.set_footer(text='KaosSpectrum Perforce Commit Bot', ts=True)
    message.send()

  else:
    return

def init():
  timer = time.time()

  while True:
    connect()
    post()
    p4.disconnect()
    time.sleep(30.0 - ((time.time() - timer) % 30.0))

p4 = P4()
init()
