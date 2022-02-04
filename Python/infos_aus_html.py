from cgitb import text
from bs4 import BeautifulSoup
import soupsieve as sv

import requests
import re
import os
import json


link="_https://www.fussball.de/spieltagsuebersicht/2-kreisklasse-a-kreis-havelland-2kreisklasse-herren-saison2122-brandenburg/-/staffel/02ET987VEO00000LVS5489B4VT8SVH36-G"

def vereinslinks_laden(link, linkart, linkliste):
    link= ohne_unterstrich(link)
    antwort = requests.get(link)
    print(antwort.status_code)
    soup = BeautifulSoup(antwort.content, 'html.parser')
    soup = soup.find(id="fixture-league-tables")
    print(type(soup))
    if soup:
        print("True")
    if soup:
        club_wrapper = (sv.select("a:is(.club-wrapper)", soup))
        linkliste[linkart] = {}
        i = 0
        for item in club_wrapper:
            link=re.findall(r'https:.*"', str(item))
            linkliste[linkart][i]=link
            i+=1

        
        
    return linkliste



def ohne_unterstrich(variable):
    
    if variable[0] == "_": 
        variable= variable[1:]
        
    elif re.findall(r'.*https:.*]', str(variable)):
        variable = str(variable)
        variable =variable[3:len(variable)-2]
        
    else:
        print("ging nicht")

    return variable


linkliste = {}

#print(requests.get("https://www.fussball.de/spieltagsuebersicht/bfv-kreisklasse-a2-karlsruhe-kreis-karlsruhe-kreisklasse-a-herren-saison2122-baden/-/staffel/02E9GSFS6G00000LVS5489B3VT07RQKQ-G").content)

#print(vereinslinks_laden(link, "Abc",linkliste))