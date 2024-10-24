#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 14:28:54 2022

@author: antonomaz
"""

import json
import Levenshtein
import glob
import re

#def lire_fichier (chemin):
#    with open(chemin) as json_data: 
#        dist =json.load(json_data)
#        
#        return dist
def lire_fichier_txt (chemin):
    f = open(chemin , encoding = 'utf−8')
    chaine = f.read ()
    f.close ()
    return chaine

#s1 = "Bonjour je suis caroline, je ne vous connais pas"
#s2="Bonjour je suis caroline"
#s3 = "Aurevoir je suis caroline"
#
#Texte1 =lire_fichier("../DATA/corpora_stanza_NER_CONCAT_PREP/ADAM/ADAM_kraken-base/ADAM_MOD/ADAM_Mon-village_Kraken-base.txt_stanza.json-concat.json")
#Texte2 =lire_fichier("../DATA/corpora_stanza_NER_CONCAT_PREP/ADAM/ADAM_kraken-base/ADAM_PP/ADAM_Mon-village_PP.txt_stanza.json-concat.json")

#def leven_dist(texteA, texteB):
#    dico = {}
##    lev = Levenshtein.distance(texteA, texteB)
#    ratio1 = Levenshtein.ratio(texteA, texteB)
#    dico["Levenshtein"] = ratio1
##    print(lev)
##    print(ratio1)
#    return dico

def leven_dist(texteA, texteB, liste_name =["Levenshtein", "Jaro-Winkler"]):
    dico = {}
    for metric_name in liste_name :
#    lev = Levenshtein.distance(texteA, texteB)
        if metric_name != "Levenshtein":
            jaro1=Levenshtein.jaro_winkler(texteA, texteB)
            dico[metric_name] = jaro1
        
        
        else:
            ratio1 = Levenshtein.ratio(texteA, texteB)
            dico[metric_name] = ratio1
            
#    print(lev)
#    print(ratio1)
    return dico

def stocker( chemin, contenu):

    w =open(chemin, "w")
    w.write(json.dumps(contenu , indent = 2))
    w.close()
    print(chemin)

for subcorpus in glob.glob('../DATA/corpora_SAPCY2.3.5-EN_CONCAT_JSON_part1/*/*'):
    print(subcorpus)
    
    outputs = glob.glob(f"{subcorpus}/*/*")
    dico_out = {}
    dist_txt = {}
    for file_type in ["txt", "json"]:
        chemins = [x for x in outputs if len(re.findall(f"{file_type}$",x))>0]
        liste_compare = []
        for path_file in chemins:
            filename = re.split("/", path_file)[-1]
            elems = re.split("_|\\.", filename)
            print("ELEMS",elems)
            auteur,titre, version, modele = elems[0], elems[1],elems[-2], elems[-3]
            if file_type =="txt":
                liste_compare.append([version, lire_fichier_txt(path_file)])
            else:
                with open (path_file) as f :
                    liste = json.load(f)
                chaine = " ".join(liste)
                liste_compare.append([modele, chaine])
#                print(liste_compare)
        for c in liste_compare:
            print(file_type, c[0])
        dico_out[file_type] = {}
        for ID1 in range(len(liste_compare)):
            print("ID1",ID1)
            version1 = liste_compare[ID1][0]
#            print("version1",version1)
            for ID2 in range(ID1+1, len(liste_compare)):
                print("ID2",ID2)
                version2 = liste_compare[ID2][0]
#                print("version2",version2)
                dico_dist =leven_dist(liste_compare[ID1][1], liste_compare[ID2][1])
                paire = "%s--%s"%(version1, version2)
                dico_out[file_type][paire] = dico_dist
#    
#    
#       
    stocker("%s_Spacy-lg_LEV-SIM-concat-word.json"%(subcorpus), dico_out)