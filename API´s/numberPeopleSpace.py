import requests

api_url = "http://api.open-notify.org/astros.json"


payload = "{\n\t\"message\": \"success\",\n\t\"number\": NUMBER_OF_PEOPLE_IN_SPACE,\n\t\"people\": [{\n\t\t\"name\": NAME,\n\t\t\"craft\": SPACECRAFT_NAME\n\t}]\n}"
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "f4f05908-5bfe-4146-b8e0-d7cdcbc64436"
    }

response = requests.request("GET", api_url, data=payload, headers=headers)

formated_response = response.json()

#print(response.text)
#print(formated_response['number'])
print("En este momento hay " + formated_response['number'] + " personas en el espacio.")