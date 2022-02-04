from importlib import import_module


import wettbewerbe_laden
import tabellen_erhalten

verbaende = wettbewerbe_laden.wettbewerb_laden()
tabellen_erhalten.links_erzeugen(verbaende,"_2122","_1")