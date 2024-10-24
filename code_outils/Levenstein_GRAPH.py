#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 07:55:13 2022

@author: antonomaz
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 12:25:50 2021

@author: antonomaz
"""


import glob , json, re

import matplotlib.pyplot as plt
import numpy as np


def lire_fichier (chemin):
    with open(chemin) as json_data: 
        dist =json.load(json_data)

    
    return dist

def nom_fichier(chemin):
    for mot in glob.glob(chemin): 
        noms_fichiers = re.split("/", chemin)
        nomsfich = re.split("\.",  noms_fichiers[6])
        nomsfich = re.split("_",  nomsfich[0])
        nmfich = nomsfich[0]
        
        return nmfich

def nom_version(chemin):
    for mot in glob.glob(chemin): 
        noms_versions = re.split("/", chemin)
        nomsvers = re.split("\.",  noms_versions[6])
        nomsvers = re.split("_",  nomsvers[0])
        nmversion = nomsvers[1]
        
        return nmversion

#def point_txt(liste_tesseract_fra,liste_tesseract_bn,liste_tesseract_png,liste_kraken_base, dist_txt, liste_name_metric):
def point_txt(liste_tesseract_fra,liste_tesseract_frabn,liste_tesseract_png,liste_kraken_base, dist_txt,liste_name_metric) :
     
    x=["Tess-Fra","Tess-Fra-bin","Tess-png","Kraken"]
#    x=["Tess-Fra","Tess-bin","Tess-png","Kraken"]
    #Levenshtein = 0
    point_txt = [liste_tesseract_fra[0][0],liste_tesseract_frabn[0][0],liste_tesseract_png[0][0],liste_kraken_base[0][0] ] 
#    point_txt = [liste_tesseract_fra[0][0],liste_tesseract_bn[0][0],liste_tesseract_png[0][0],liste_kraken_base[0][0] ]
    plt.scatter(x, point_txt , label = (" ".join([liste_name_metric[0]," Ref. vs OCR Version"])), s=20, marker="v")

    #Jaro-Winkler = 1
#    point_txt = [liste_tesseract_fra[0][1],liste_tesseract_bn[0][1],liste_tesseract_png[0][1],liste_kraken_base[0][1]]
    point_txt = [liste_tesseract_fra[0][1],liste_tesseract_frabn[0][1],liste_tesseract_png[0][1],liste_kraken_base[0][1]]
    plt.scatter(x, point_txt , label = (" ".join([liste_name_metric[1]," Ref. vs OCR Version"])), s=20, marker="<")


    plt.ylabel("Distances")
    plt.xlabel("OCR Version ")
    plt.axis([-1,4.5,0,1]) 


#def point_stz(liste_tesseract_fra,liste_tesseract_bn,liste_tesseract_png,liste_kraken_base, dist_stz, liste_name_metric):
def point_stz(liste_tesseract_fra,liste_tesseract_frabn,liste_tesseract_png,liste_kraken_base, dist_stz,liste_name_metric):
     
    x=["Tess-Fra","Tess-Fra-bin","Tess-png","Kraken"]
#    x=["Tess-Fra","Tess-bin","Tess-png","Kraken"]
    #Levenshtein = 0
#    point_stz = [liste_tesseract_fra[1][0],liste_tesseract_bn[1][0],liste_tesseract_png[1][0],liste_kraken_base[1][0] ] 
    point_stz = [liste_tesseract_fra[1][0],liste_tesseract_frabn[1][0],liste_tesseract_png[1][0],liste_kraken_base[1][0] ] 
    plt.scatter(x, point_stz , label = (" ".join([liste_name_metric[0],dist_stz[-1]])), s=20, marker="v")
  
    # Jaro-Winkler = 1
#    point_stz = [liste_tesseract_fra[1][1],liste_tesseract_bn[1][1],liste_tesseract_png[1][1],liste_kraken_base[1][1]]  
    point_stz = [liste_tesseract_fra[1][1],liste_tesseract_frabn[1][1],liste_tesseract_png[1][1],liste_kraken_base[1][1]]  
    plt.scatter(x, point_stz , label = (" ".join([liste_name_metric[1],dist_stz[-1]])), s=20, marker="<")
    
   
    plt.ylabel("Distances")
    plt.xlabel("OCR Version ")
    plt.axis([-1,4.5,0,1])  

   
def stocker_graph_txt(nomfich): 
    
    name_fig = "%s.png"
    print(" nom de la figure ", name_fig)
#    
    plt.legend(loc="lower left",ncol=1, bbox_to_anchor=(0,0.98))
    plt.legend 
    plt.savefig(nomfich)
    plt.clf()
    
    return nomfich

def stocker_graph(nomfich): 
    
    name_fig = "%s.png"
    print(" nom de la figure ", name_fig)
#    
    plt.legend(loc="lower left",ncol=2, bbox_to_anchor=(0.1,0.98))
    plt.legend 
    plt.savefig(nomfich)
    plt.clf()
    
    return nomfich



### MAIN

dist_txt=[]
dist_stanza=[]


liste_kraken_base =[]
liste_kraken_17 =[]
liste_tesseract_fra =[]
liste_tesseract_frabn =[]
liste_tesseract_png =[]
liste_tesseract_bn =[]
liste_name_metric=["Levenshtein", "Jaro-Winkler"]


#path_corpora ="../DATA/SPACY2.3.5/corpora_SPACY2.3.5-EN_CONCAT_JSON_GRAPH_DIST_part1/TESS-BIN/*/"
path_corpora ="../DATA/SPACY2.3.5/corpora_SPACY2.3.5-EN_CONCAT_JSON_GRAPH_DIST_part1/TESS-FRA-BIN/*/"
for chemin in glob.glob(path_corpora):
#    print ("***********CHEMIN",chemin)
    liste_kraken_base =[]
    liste_kraken_17 =[]
    liste_tesseract_fra =[]
    liste_tesseract_png =[]
    liste_tesseract_bn =[]
    liste_tesseract_frabn =[]
#
    for chemin_fichier in glob.glob("%s/*.json"%chemin):
#        print(chemin_fichier)
        path_dist=lire_fichier(chemin_fichier)
        print(path_dist)
        nomfichier= nom_fichier(chemin_fichier)
        nomversion = nom_version(chemin_fichier)
        print(chemin)
        print(nomfichier)
        print(nomversion)
        print(path_corpora)
    
        dist_txt=[]
        dist_stanza=[]
        
        
#
#        
        version_OCR = nomversion
        print(version_OCR)
  
        modele_version = list(path_dist['json'].keys())
#        print("modele_version :",jsonversion)
        
        for cle, dic in path_dist.items(): 
#                
#            print("l'élément de clé", cle)
#            
#                
#                
            for version, modele in dic.items():
                for name_metric, liste in modele.items():
                    print("LISTE",liste)
#                            liste_name_metric.append(name_metric)
                    liste= [liste]      
                    for resultat in liste:

                            if cle == "txt" :
                                
                                dist_txt.append(1-resultat)
                               
               
                            if version == "spacy--spacy" :
                                
                                dist_stanza.append(1-resultat)

                                       
                                
                                    
                                    
        
        
        dist_txt.append("txt")
        dist_stanza.append("SpaCy-lg")
        
#        print("-------SM",dist_sm)
#        print("--------MD",dist_md)
#        print("----------LG",dist_lg)        
#                
#        if version_OCR == "TESSERACT-BIN":
#
#            liste_tesseract_bn.append(dist_txt)
#            liste_tesseract_bn.append(dist_stanza)
            

            
#                
        if version_OCR == "TESSERACT-PNG":
            
            liste_tesseract_png.append(dist_txt)
            liste_tesseract_png.append(dist_stanza)
            
                
        if version_OCR == "TesseractFra-PNG":
           
            liste_tesseract_fra.append(dist_txt)
            liste_tesseract_fra.append(dist_stanza)
            
        
        if version_OCR == "TesseractFra-BIN":
            liste_tesseract_frabn.append(dist_txt)
            liste_tesseract_frabn.append(dist_stanza)
#            
                
        if version_OCR == "kraken-base":
            
            liste_kraken_base.append(dist_txt)
            liste_kraken_base.append(dist_stanza)
           
        
#print(liste_kraken_base) 

#    point_txt(liste_tesseract_fra,liste_tesseract_bn,liste_tesseract_png,liste_kraken_base, dist_txt,liste_name_metric)
    point_txt(liste_tesseract_fra,liste_tesseract_frabn,liste_tesseract_png,liste_kraken_base, dist_txt,liste_name_metric)
    stocker_graph_txt("../DATA/SPACY2.3.5/corpora_SPACY2.3.5-EN_CONCAT_JSON_GRAPH_DIST_part1/OUTPUT_GRAPH/%s_SpaCy-lg_graph-dist_%s"%(nomfichier, dist_txt[-1])) 
    
#    point_stz(liste_tesseract_fra,liste_tesseract_bn,liste_tesseract_png,liste_kraken_base, dist_stanza,liste_name_metric)
    point_stz(liste_tesseract_fra,liste_tesseract_frabn,liste_tesseract_png,liste_kraken_base, dist_stanza,liste_name_metric)
    stocker_graph("../DATA/SPACY2.3.5/corpora_SPACY2.3.5-EN_CONCAT_JSON_GRAPH_DIST_part1/OUTPUT_GRAPH/%s_SpaCy-lg_graph-dist_%s"%(nomfichier, dist_stanza[-1])) 
    
         
        

     
    

    
    
    
    