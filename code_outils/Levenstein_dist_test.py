#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 20:36:20 2022

@author: antonomaz
"""
import Levenshtein

def leven_dist(texteA, texteB, liste_name =["Levenshtein", "jaro"]):
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

texte1="Bonjour, je suis caroline"
texte2="Salut, je suis caroline"

LevTest = leven_dist(texte1,texte2)
print(LevTest)

ration2 =Levenshtein.ratio(texte1, texte2)
print(ration2)
#
jaro1=Levenshtein.setratio(texte1, texte2)
print(jaro1)