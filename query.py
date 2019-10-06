#by Bad-DDoS
import requests
import json
key = "KEY"
query = "QUERY SHODAN"
api = requests.get('https://api.shodan.io/shodan/host/search?key=' + key + '&query=' + query)
result = api.text
json_decode = json.loads(result)
matches = json_decode['matches']
f = open("shodan_api.txt", "a")
for value in matches:
	f.write(value['ip_str'] + "\n")
f.close()
print("Ok")
