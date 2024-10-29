
import json
import glob
import re

# import pour graphique
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def lire_fichier (chemin):
   with open(chemin) as json_data:
       dist =json.load(json_data)
   return dist


def stocker_graph(nomfich):
    name_fig = "%s.png"
    print(" nom de la figure ", name_fig)
    #
    # plt.legend(loc="lower left", ncol=1, bbox_to_anchor=(0, 0.98))
    plt.legend(loc="lower left", ncol=2, bbox_to_anchor=(0.1, 0.98))
    plt.legend
    plt.savefig(nomfich)
    plt.clf()
    return nomfich


def save_graph_moustache(nomfich):
    plt.savefig(nomfich, dpi=300, bbox_inches="tight")
    plt.close()


def generation_graph_moustache(tab, stype, bsave=False):
    size = [1]

    path_data = f"../ARTICLE_CORPUS/small-*"  ##
    #
    # data_tab_krakcos = tab.query("Version == 'Kraken-base' and Dist_type == 'cosinus'")
    # liste_krakcos = data_tab_krakcos["Version"] + " " + data_tab_krakcos["Dist_type"]
    # data_tab_tescos = tab.query("Version == 'TesseractFra-PNG' and Dist_type == 'cosinus'")
    # liste_tescos = data_tab_tescos["Version"] + " " + data_tab_tescos["Dist_type"]
    # data_tab_kraklev = tab.query("Version == 'kraken-base' and Dist_type == 'Levenshtein'")
    # liste_kraklev = data_tab_kraklev["Version"] + " " + data_tab_kraklev["Dist_type"]
    # data_tab_teslev = tab.query("Version == 'TesseractFra-PNG' and Dist_type == 'Levenshtein'")
    # liste_teslev = data_tab_teslev["Version"] + " " + data_tab_teslev["Dist_type"]
    #
    for x in size:
        sns.set_theme(style="ticks")
    #
        # Initialize the figure with a logarithmic x axis
        # f, ax = plt.subplots(figsize=(15,32))
        f, ax = plt.subplots(figsize=(15, 15))
        ax.set_xscale("linear")
    #
    #     # Plot the orbital period with horizontal boxes
        sns.boxplot(x="Distances", y="configuration", data=tab,
                    whis=[0, 1], width=.6,
                    palette="colorblind"  #"coolwarm"
                    )  # , legend=False)#
    #     sns.boxplot(x="Distances", y=liste_kraklev, data=data_tab_kraklev,
    #                 whis=[0, 1], width=.6,
    #                 palette="colorblind")  # , legend=False)#
    #     sns.boxplot(x="Distances", y=liste_tescos, data=data_tab_tescos,
    #                 whis=[0, 1], width=.6,
    #                 palette="colorblind")  # , legend=False)#
    #     sns.boxplot(x="Distances", y=liste_teslev, data=data_tab_teslev,
    #                 whis=[0, 1], width=.6,
    #                 palette="colorblind")  # , legend=False)#
    #
    #     # Add in points to show each observation
    #     sns.stripplot(x="Distances", y=liste_krakcos, data=data_tab_krakcos,
    #                   size=4, palette='dark:.3',
    #                   linewidth=0)  # , legend=False)#
    #     sns.stripplot(x="Distances", y=liste_kraklev, data=data_tab_kraklev,
    #                   size=4, palette='dark:.3',
    #                   linewidth=0)  # , legend=False)#
    #     sns.stripplot(x="Distances", y=liste_tescos, data=data_tab_tescos,
    #                   size=4, palette='dark:.3',
    #                   linewidth=0)  # , legend=False)#
    #     sns.stripplot(x="Distances", y=liste_teslev, data=data_tab_teslev,
    #                   size=4, palette='dark:.3',
    #                   linewidth=0)  # , legend=False)#
        sns.stripplot(x="Distances", y="configuration", data=tab,
                      size=4, palette='dark:.3',
                      linewidth=0)  # , legend=False)#

        # Tweak the visual presentation
        plt.tick_params(axis='both', labelsize=25)
        ax.xaxis.grid(True)
        ax.set(ylabel="")
        plt.xlim([0, x])

        ## sauvegarde du graphe
        if bsave == True:
            nomgraph = f"./test_size-{stype}-{x}.png"
            save_graph_moustache(nomgraph)


def get_cosinus_folder_nom_version(chemin):
    noms_versions = re.split("/", chemin)
    nomsvers = re.split("_", noms_versions[-2])
    nmversion = nomsvers[-1]
    return nmversion


def get_cosinus_ref_REN_type(chemin):
    part_chemin = re.split("_", chemin)
    part_chemin1 = re.split("\.", part_chemin[-1])
    nomsRENs = part_chemin1[-2]
    return nomsRENs


def get_cosinus_ref_OCR_type(chemin):
    part_chemin = re.split("_", chemin)
    part_chemin1 = re.split("\.", part_chemin[-1])
    nomsOCRs = part_chemin1[-3]
    return nomsOCRs


def get_cosinus_ocr_REN_type(chemin):
    part_chemin = re.split("_", chemin)
    part_chemin1 = re.split("-", part_chemin[-1])
    nomsRENs = part_chemin1[0] + part_chemin1[1] + part_chemin1[2]
    return nomsRENs


def get_cosinus_ocr_OCR_type(chemin):
    part_chemin = re.split("_", chemin)
    part_chemin1 = re.split("\.", part_chemin[-2])
    nomsOCRs = part_chemin1[0]
    return nomsOCRs


def get_lev_REN_type(chemin):
    part_chemin = re.split("_", chemin)
    nomsRENs = part_chemin[-2]
    return nomsRENs


def get_lev_OCR_type(chemin):
    part_chemin = re.split("_", chemin)
    nomsOCRs = part_chemin[-3]
    return nomsOCRs


dico_global = {}
Liste_global_version_ocr = []
Liste_global_REN = []
Liste_global_type_distance = []
Liste_global_valeur_distance = []
liste_folder_OCR_OK = ["kraken", "TesseractFra-PNG"]
liste_file_OCR_OK = ["kraken-base", "TesseractFra-PNG"]
liste_config = []
### récupération des données cosinus
mykey = "cosinus"
for subcorpus in glob.glob("../DATA/small-ELTeC-fra_spaCy2.3.5_cosinus/*/*/*/SIM"):
    # print(subcorpus)
    ## on vérifie que l'OCR est dans la liste, sinon on ne fait rien
    folder_version = get_cosinus_folder_nom_version(subcorpus)
    if folder_version in liste_folder_OCR_OK:
        ## récupération données référence
        for chemin_fichier in glob.glob("%s/*.json" % subcorpus):
            # print(chemin_fichier)
            # récupération version REN dans le nom du fichier
            VersionREN = get_cosinus_ref_REN_type(chemin_fichier)
            # récupération version OCR dans le nom du fichier
            VersionOCR = get_cosinus_ref_OCR_type(chemin_fichier)
            # lecture du fichier json
            jsonfile = lire_fichier(chemin_fichier)
            Liste_global_version_ocr.append(VersionOCR)
            Liste_global_REN.append(VersionREN)
            Liste_global_type_distance.append(mykey)
            liste_config.append(VersionOCR + " -- " + mykey)
            # récupération distance cosinus
            Liste_global_valeur_distance.append(jsonfile[mykey][0])

        ## récupération données REN
        ocrSubcorpus = subcorpus[:-3] + "NER/SIM"
        for chemin_fichier in glob.glob("%s/*.json" % ocrSubcorpus):
            # print(chemin_fichier)
            # récupération version REN dans le nom du fichier
            VersionREN = get_cosinus_ocr_REN_type(chemin_fichier)
            # print("VersionREN :", VersionREN)
            if VersionREN == "spacylg2.3.5":
                # print("VersionREN :", VersionREN)
                # récupération version OCR dans le nom du fichier
                VersionOCR = get_cosinus_ocr_OCR_type(chemin_fichier)
                # print("VersionOCR :", VersionOCR)
                # lecture du fichier json
                jsonfile = lire_fichier(chemin_fichier)
                Liste_global_version_ocr.append(VersionOCR)
                Liste_global_REN.append(VersionREN)
                Liste_global_type_distance.append(mykey)
                liste_config.append(VersionOCR + " -- " + mykey)
                # récupération distance cosinus
                Liste_global_valeur_distance.append(jsonfile[mykey][0])

### récupération des données levenstein
type_distance = "Levenshtein"
for subcorpus in glob.glob("../DATA/small-ELTeC-fra_REN_spaCy2.3.5_Levenshtein/*"):
    # print(subcorpus)
    for chemin_fichier in glob.glob("%s/*.json" % subcorpus):
        print(chemin_fichier)
        ## récupération version OCR dans le nom du fichier
        VersionOCR = get_lev_OCR_type(chemin_fichier)
        # print(VersionOCR)
        if VersionOCR in liste_file_OCR_OK:
            ## récupération version REN dans le nom du fichier
            VersionREN = get_lev_REN_type(chemin_fichier)
            ## lecture du fichier json
            jsonfile = lire_fichier(chemin_fichier)

            ## référence
            mykey = "txt"
            Liste_global_version_ocr.append(VersionOCR)
            Liste_global_REN.append(mykey)
            Liste_global_type_distance.append(type_distance)
            liste_config.append(VersionOCR +" -- "+type_distance)
            ## récupération distance Levenshtein
            listekey = jsonfile[f"{mykey}"].keys()
            Liste_global_valeur_distance.append(jsonfile[f"{mykey}"][f"{list(listekey)[0]}"][type_distance])

            ## donnée REN
            mykey = "json"
            Liste_global_version_ocr.append(VersionOCR)
            liste_config.append(VersionOCR+" -- "+type_distance)
            Liste_global_REN.append(VersionREN)
            Liste_global_type_distance.append(type_distance)
            ## récupération distance Levenshtein
            listekey = jsonfile[f"{mykey}"].keys()
            Liste_global_valeur_distance.append(jsonfile[f"{mykey}"][f"{list(listekey)[0]}"][type_distance])

### création d'un dictionnaire global
dico_global["configuration"] = liste_config
dico_global["Version"] = Liste_global_version_ocr
dico_global["REN"] = Liste_global_REN
dico_global["Dist_type"] = Liste_global_type_distance
dico_global["Distances"] = Liste_global_valeur_distance
# print(dico_global)

### création d'un dataframe
data_tab = pd.DataFrame(dico_global)
data_tab=data_tab.sort_values(by = 'configuration')
print(data_tab)
## création d'un dataframe pour la référence
data_tabtxt = data_tab.query("REN == 'txt' ")
# print(data_tabtxt)
## création d'un dataframe pour spacy-lg
data_tabspacy = data_tab.query("REN != 'txt' ")
# print(data_tabspacy)

### création des graphiques
generation_graph_moustache(data_tabtxt, "txt", True)
generation_graph_moustache(data_tabspacy, "spacy-lg", True)
