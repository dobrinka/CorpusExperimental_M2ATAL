# -*- coding: utf-8 -*-
import os
import re
import subprocess
from tabulate import tabulate

#Sortie des résultats globals
def global_results(languages, utils):
	for langue in languages:
		for util in utils:
			global_path = "./resultats/%s/"%util + "GlobalStatisticResults/%s/"%langue
			files_HTML = "./resultats/%s/"%util +"%s/"%langue
			files_gold = "./source/%s/gold"%langue
			if not os.path.exists(global_path):
				os.makedirs(global_path)

			for dirs in os.listdir("./resultats/%s/"%util):
				bashCommand_cleaneval = "python cleaneval.py -t ./resultats/%s"%util + "/%s/ "%langue + \
										"./source/%s/gold"%langue
				with open(global_path + "ResultsGlobales" + "%s.txt"%util, "w+") as logfile_global:
					subprocess.call(bashCommand_cleaneval, shell=True, stdout=logfile_global)


#Sortie des résultats locales
def local_results(languages):
	for langue in langues:
		local_path = "./resultats/LocalStatisticResults/%s/"%langue
		if not os.path.exists(local_path):
				os.makedirs(local_path)
		ResultsLocal = open(local_path + "ResultsLocales.txt", "w+")
		dossier_resultats = './resultats/HTML2text/%s/'%langue
		for dirName, subdirList, fileList in os.walk(dossier_resultats):
			for fname in fileList:
				match = re.search(r'.*?_([^_]+)_', '%s' % fname, re.S)
				if match:
					site_name = match.group(1)
					table = [[site_name,
							  os.system("python test_api.py -t ./resultats/HTML2text/%s/"%langue +"%s"%fname +
										"./source/%s/"%langue + "gold/%s"%fname),
							  os.system("python test_api.py -t ./resultats/jusText/%s/"%langue + "%s"%fname +
										"./source/en/gold/%s"%fname)]]
				ResultsLocal.write(tabulate(table))

langues = ["en","el","pl","ru","zh"]
utils = ["HTML2text","jusText"]
global_results(langues,utils)
local_results(langues)