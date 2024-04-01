import requests
import json
from datetime import datetime
import time


# r = requests.post("https://api.pushover.net/1/messages.json", data = {
#   "token": "am4mbd848h6kw1qj4emwibu4umwd3w",
#   "user": "u2sy4rm1rpbfj72tbzf4kf3t9hojrs",
#   "message": "hello world"
# },
# files = {
#   "attachment": ("image.jpg", open("timericon.png", "rb"), "image/png")
# })
# print(r.text)



rawrides = str(
  requests.get("https://queue-times.com/parks/2/queue_times.json").text)

# Get all ride info and times



run = True
lowqueuerides = []
newrides = []
while run:
  
  
  stealth = json.loads(
      rawrides[rawrides.find("{\"id\":91,"):rawrides.find(",{\"id\":103")])
  
  swarm = json.loads(
      rawrides[rawrides.find("{\"id\":103,"):rawrides.find(",{\"id\":5558")])
  
  saw = json.loads(
      rawrides[rawrides.find("{\"id\":104,"):rawrides.find(",{\"id\":91")])
  
  nemesis = json.loads(
      rawrides[rawrides.find("{\"id\":88,"):rawrides.find(",{\"id\":104")])
  
  colossus = json.loads(
      rawrides[rawrides.find("{\"id\":96,"):rawrides.find(",{\"id\":88")])
  
  wddr = json.loads(
      rawrides[rawrides.find("{\"id\":5558,"):rawrides.find("]},{\"id\":763")])
  
  tidal = json.loads(
      rawrides[rawrides.find("{\"id\":92,"):rawrides.find(",{\"id\":100")])
  
  rush = json.loads(
      rawrides[rawrides.find("{\"id\":98,"):rawrides.find(",{\"id\":94")])
  
  detonator = json.loads(
      rawrides[rawrides.find("{\"id\":89,"):rawrides.find(",{\"id\":4546")])
  
  storm = json.loads(
      rawrides[rawrides.find("{\"id\":94,"):rawrides.find(",{\"id\":92")])
  
  vortex = json.loads(
      rawrides[rawrides.find("{\"id\":100,"):rawrides.find(",{\"id\":101")])
  

  rides = [
      stealth, swarm, saw, nemesis, colossus, wddr, tidal, rush, detonator,
      storm, vortex
  ]
  # Print those times
  for ride in rides:
    if ride["wait_time"] < 21 and ride["is_open"] == True:
      if ride['name'] not in lowqueuerides:
        lowqueuerides.append(ride['name'])
        newrides.append(ride) 
        print(ride["name"])
    
      elif ride['wait_time'] > 20 or ride["is_open"] == False:
        lowqueuerides.remove(ride["name"])
        print(f'after removal {lowqueuerides}')

  message = ""
  counter = 1
  newnames = []
  for ride in newrides:
    newnames.append(ride['name'])
  print(lowqueuerides)
  print("^^^")
  print(len(newnames))
  print(newnames)
  if len(newnames) > 1:
    for ride in newnames:
      if len(newnames) == counter:
        message += f"and {ride} now have low queue times"
        counter += 1
      else:
        message += f"{ride}, "
        counter += 1
  elif len(newrides) == 1:
    message = f"{newrides[0]['name']}'s queue is currently walk-on"
    if newrides[0]['wait_time'] > 0:
      message = f"{newrides[0]['name']}'s queue time is currently at {newrides[0]['wait_time']} mins"
  print(message)

  if len(newrides) > 0:
    
    r = requests.post("https://api.pushover.net/1/messages.json", data = {
      "token": "am4mbd848h6kw1qj4emwibu4umwd3w",
      "user": "u2sy4rm1rpbfj72tbzf4kf3t9hojrs",
      "message": message
    },
    files = {
      "attachment": ("image.jpg", open("timericon.png", "rb"), "image/png")
    })
    print(r.text)
    
  print(f"As of {stealth['last_updated']}")
  newrides = []
  




  
  # Work out seconds from midnight (now)
  c = datetime.now()
  chour = int(c.strftime('%H'))
  cmin = int(c.strftime('%M'))
  csec = int(c.strftime('%S'))
  ctimesec = (chour * 3600) + (cmin * 60) + csec

  #Work out seconds from midnight (last updated)
  uhour = int(rawrides[rawrides.find("Z")-12:rawrides.find("Z")-10])
  umin = int(rawrides[rawrides.find("Z")-9:rawrides.find("Z")-7])
  usec = int(rawrides[rawrides.find("Z")-6:rawrides.find("Z")-4])
  
  utimesec = (uhour*3600) + (umin*60) + usec
  time.sleep(300-(ctimesec-utimesec))

  #update the file
  print("Attempting first update...")
  rawrides2 = str(
    requests.get("https://queue-times.com/parks/2/queue_times.json").text)
  i = 1
  while rawrides2 == rawrides:
    i += 1
    time.sleep(10)
    rawrides2 = str(
      requests.get("https://queue-times.com/parks/2/queue_times.json").text)
    print(f"Attempting update no {i}")
    
  rawrides = rawrides2
  print("Updated list.")