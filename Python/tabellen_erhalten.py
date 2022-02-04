# -*- coding: utf-8 -*-
from datetime import date
from operator import indexOf
import requests
import json
import os
import shutil
import infos_aus_html

# http://www.fussball.de/wam_competitions_61_2122_1_112_253_01KVSKB9F4000000VTVG0001VTS8P479.json
# http://www.fussball.de/wam_competitions_Verband_Saison_Wettkampf_Alter_Klasse_Gebiet.json
#Verband ja, Saison ja, Wettkampf ja, alter ja, klassen ja, gebiet ja

grundpath=os.path.join(os.path.dirname(os.path.dirname(__file__)),"Data")
#print(path)


#Altersklasse finden
def alter_finden(altersklasse, verbandsname):
    #JSON einladen
    path=os.path.join(grundpath, verbandsname)
    son=json.load(open(os.path.join(path,"Wettbewerbe.json"), encoding='utf-8'))

    find_key_alter = altersklasse
    result = list(son["Mannschaftsart"].values()).index(find_key_alter)
    alter=list(son["Mannschaftsart"])[result]
    
    print("Alterklassen-Schlüssel",list(son["Mannschaftsart"])[result])

    return alter

#Klassen finden
def klasse_finden(alter, verbandsname):
    #JSON einladen
    path=os.path.join(grundpath, verbandsname)
    son=json.load(open(os.path.join(path,"Wettbewerbe.json"), encoding='utf-8'))


    
    klasse= list(son["Spielklasse"][ohne_unterstrich(alter)])
    klassen=[]
    for item in klasse:
        klassen.append(item)
    print("Klassen-Schlüssel",klassen)
    return(klassen)
    
#Gebiet finden    
def gebiet_finden(alter, klasse, verbandsname):
    #JSON einladen
    path=os.path.join(grundpath, verbandsname)
    son=json.load(open(os.path.join(path,"Wettbewerbe.json"), encoding='utf-8'))

    

    gebiet= son["Gebiet"][str(ohne_unterstrich(alter))][str(ohne_unterstrich(klasse))]
    gebiete=[]
    for item in gebiet:
        gebiete.append(item)
    return gebiete



verbaende={'Deutschland': '_89', 'Baden': '_32', 'Bayern': '_31', 'Berlin': '_66', 'Brandenburg': '_61', 'Bremen': '_02', 'Hamburg': '_03', 'Hessen': '_34', 'Mecklenburg-Vorpommern': '_62', 'Mittelrhein': '_23', 'Niederrhein': '_22', 'Niedersachsen': '_01', 'Rheinland': '_41', 'Saarland': '_43', 'Sachsen': '_63', 'Sachsen-Anhalt': '_64', 'Schleswig-Holstein': '_04', 'Südbaden': '_33', 'Südwest': '_42', 'Thüringen': '_65', 'Westfalen': '_21', 'Württemberg': '_35'}

def links_erzeugen(verbaende, saison, wettkampf):
    verbandsnamen= list(verbaende.keys())
    verbandsnummern= list(verbaende.values())
    for verband in verbandsnamen:
        index= verbandsnamen.index(verband)
        verbandsnummer= verbandsnummern[index]
        print(index)
        altersklasse=alter_finden("Herren", verband)
        spielklasse= klasse_finden(altersklasse, verband)
        linkliste={}
        for klasse in spielklasse:
            print(altersklasse)
            print(klasse)
            print(verband)
            gebiete= gebiet_finden(altersklasse, klasse, verband)
            
            for gebiet in gebiete:
                linkart='"'+verband+"_"+klasse+"_"+gebiet+'"'
                link="http://www.fussball.de/wam_competitions"+verbandsnummer+saison+wettkampf+altersklasse+klasse+gebiet+".json"

                recive=json.loads(requests.get(link).content)
                ergebnis = list((recive[ohne_unterstrich(klasse)][ohne_unterstrich(gebiet)].keys()))
                #print(ergebnis)
                linkliste = infos_aus_html.vereinslinks_laden(ergebnis, linkart, linkliste)
        
                linkliste_json=json.dumps(linkliste, indent = 4)
                dirpath=os.path.join(grundpath, verband)
                save= open(os.path.join(dirpath, "Vereinslinks.json"),"w")
                save.write(linkliste_json)
                save.close()    


            
def ohne_unterstrich(variable):
    if variable[0] == "_": variable= variable[1:]
    return variable







links_erzeugen(verbaende,"_2122","_1")





# altersklasse = alter_finden("Herren")
# klassen = klasse_finden(altersklasse)
# print(klassen)
#print(gebiet_finden(112,253,"Brandenburg"))



# verbandsnamen= list(verbaende.keys())
# verbandsnummern= list(verbaende.values())        

# index= verbandsnamen.index("Brandenburg")

# print(index)
# print(verbandsnummern[index])