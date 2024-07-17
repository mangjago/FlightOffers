import requests

def get_airports_name(city):
  url = f"https://testapi.aviowiki.com/free/airports/search?query={city}"
  response = requests.get(url)
  iata = []
  name = []
  for data in response.json()["content"]:
    if data["iata"] == None:
      pass
    else:
      name.append(data["name"])
      iata.append(data["iata"])
  
  return iata, name