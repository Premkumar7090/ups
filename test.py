import requests

url = "https://translation.googleapis.com/language/translate/v2"

querystring = {"key":"AIzaSyAZuEHsxe7s_swEIkBKJETznel05naET_8"}

payload = {
    "q": "",
    "source": "",
    "target": "",
    "format": "text"
}
payload['q']="hi"
payload['source']='en'
payload['target']='fr'
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, json=payload, headers=headers, params=querystring)


data = response.json()


response1 = data['data']['translations'][0]['translatedText']
print(response1)