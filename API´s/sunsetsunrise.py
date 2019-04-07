import requests
import json
import urllib3


##############################################################
# sunsetSunrise.py
# [X]v1 mostrar hora de amanecer y puesta de sol para unas coordenadas 
# dadas
#
##############################################################


requests.packages.urllib3.disable_warnings()
#Data query
api_url = "https://api.sunrise-sunset.org/json"
my_lat = 44.441457
my_lng = -3.642394

querystring = {
    "lat":"44.441457",
    "lng":"-3.642394"
    }

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "490a2b98-0ca6-434d-9f12-3c83c88b35b5"
    }
# Como la peticion no contiene cuerpo al ser de tipo get no es necesario formatear los datos al pasarlos 

#Query 
response = requests.request("GET", api_url, data=payload, headers=headers, params=querystring)

#Data Formatting

response_formated = response.json()

print("Para las coordenadas latitud: " + str(my_lat) + " y longitud: " + str(my_lng) + 
" Las hora prevista para el amanecer es " + response_formated['results']['sunrise'] + 
" y la puesta de sol  " + response_formated['results']['sunset'] +". El día tendrá una duración de " + response_formated['results']['day_length'] + " horas")



