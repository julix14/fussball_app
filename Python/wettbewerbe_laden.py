# -*- coding: utf-8 -*-
from datetime import date
from traceback import print_tb
import requests
import json
import os
import shutil
var_verband=""
link="http://www.fussball.de/wam_kinds"+var_verband+"_2122_1.json"

#Pfad des JSON Datei suchen
path=os.path.join(os.path.dirname(os.path.dirname(__file__)),"JSON")
#JSON öffnen und speichern
son=json.load(open(os.path.join(path,"wam_base.json"), encoding='utf-8'))

verbaende= son["Mandanten"]
verbaende = {value:key for key, value in verbaende.items()}

datenpfad=os.path.join(os.path.dirname(os.path.dirname(__file__)),"Data")




def wettbewerb_laden():
    for verband in verbaende.keys():
        dirpath=os.path.join(datenpfad, verband)
        if  os.path.exists(dirpath)== False:
            os.makedirs(dirpath)    
        
        #Zeile löscht die erstellten verzeichnisse wieder
        #else :
        #  shutil.rmtree(os.path.join(datenpfad, verband))

        var_verband=verbaende[verband]
        link="http://www.fussball.de/wam_kinds"+var_verband+"_2122_1.json"
        recive= requests.get(link)
        print(link)
        print(recive.status_code)
        
        save= open(os.path.join(dirpath, "Wettbewerbe.json"),"wb")
        save.write(recive.content)
        save.close()
        
        print("Datei "+os.path.join(dirpath, "Wettbewerbe.json")+" erstellt")
    return(verbaende)
print(list(verbaende.keys())[0])
