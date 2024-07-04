import json
import sys
import requests


if len(sys.argv) != 2:
    sys.exit()

response = requests.get("http://itunes.apple.com/search?entity=song&limit=50&term=weezer")

o = response.json()
for result in o["result"]:
    print(result["trackname"])

