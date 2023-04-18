#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 20:41:12 2022

@author: harrisonplume
"""

from tinydb import TinyDB, Query
import requests
import json, re, sys, argparse, os
from datetime import datetime

os.environ['ACW_API_KEY'] = 'QGwe0goBcAcWcYqcg5Kwth9OoAoVzfzg'

db = TinyDB('accuw_db.json')
Location = db.table('Location')
Profile = db.table('Profile')

if "ACW_API_KEY" in os.environ:
    API_KEY = os.environ['ACW_API_KEY']   
    Profile.upsert({'api_key':API_KEY}, Query().api_key.exists())
else: 
    API_KEY = Profile.search(Query().api_key)
    if API_KEY == []: 
      sys.exit("No API key found")
    API_KEY = API_KEY[0]['api_key']
    
def is_input_inputted(input_var, table, field_name):
  if input_var is None: 
    input_var = table.search(Query()[field_name])
    if input_var == []: 
      parser.print_help()
      sys.exit()
    input_var = input_var[0][field_name]  
  else: 
    table.upsert({field_name:input_var}, Query()[field_name].exists())
  return input_var
 
parser = argparse.ArgumentParser(description='AccuWeather Forecast for Python')
parser.add_argument('-l', action="store", dest="location",  help='location for weather forecast, e.g. "Tokyo"') 
parser.add_argument('-m', action="store", dest="metric", choices=['c', 'f'], help='metric for weather forecast, c or f', default="c", type=str.lower )
args = parser.parse_args()
 
location = is_input_inputted(args.location,Profile, "last_location")     
metric = is_input_inputted(args.metric, Profile, "last_metric")

def getJSONfromUrl(url): 
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data
 
if (Location.count(Query()) == 0): 
  url = f"http://dataservice.accuweather.com/locations/v1/topcities/150?apikey={API_KEY}"
  json_data = getJSONfromUrl(url)
 
  for p in json_data:
    Location.insert({'name': p['LocalizedName'], 'key': p['Key'], 'english_name':p['EnglishName'],
    'administrative_area':p['AdministrativeArea']['ID'], 'country': p['Country']['EnglishName']})
    
location_from_db = Location.search(Query().name.matches(location, flags=re.IGNORECASE))
 
if location_from_db == []:
  url = f"http://dataservice.accuweather.com/locations/v1/search?apikey={API_KEY}&amp;q={location}"
  json_data = getJSONfromUrl(url)
if json_data == []:
  sys.exit(f"No location found for '{location}' from AccuWeather API") 
else:
  for p in json_data:
     Location.insert({'name': location, 'key': p['Key'], 'english_name':p['EnglishName'],
     'administrative_area':p['AdministrativeArea']['ID'],'country': p['Country']['EnglishName']})
     break
  location_from_db = Location.search(Location.name.matches(location, flags=re.IGNORECASE))
 
location_key = location_from_db[0]['key']
admin_area = location_from_db[0]['administrative_area']
country = location_from_db[0]['country']

def getFormattedDateTime(datestr):
  p_datestr_format = ''.join(datestr.rsplit(":", 1))
  date_object = datetime.strptime(p_datestr_format, '%Y-%m-%dT%H:%M:%S%z')
  return date_object.strftime("%H:%M %A, %d %B %Y Timezone:%z")
 
url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={API_KEY}&amp;details=true"
json_data = getJSONfromUrl(url)
unit = "Metric" if (metric == "c") else "Imperial"
metric_tag = "true" if (metric == "c") else "false"
 
for p in json_data:
  current_weather=p["WeatherText"]
  current_temp=p["Temperature"][unit]
  wind_speed=p["Wind"]["Speed"][unit]
  date_w_format = getFormattedDateTime(p["LocalObservationDateTime"])
 
char_length = 50
print(f"Location: {location}, {admin_area}, {country}") 
print(f"Local observation time: {date_w_format}")
print(f"Current weather status: {current_weather}")
print(f"Current temperature: {current_temp['Value']} {current_temp['Unit']}")
print(f"Wind speed: {wind_speed['Value']} {wind_speed['Unit']}")
print(f"\n{'='*char_length}")
