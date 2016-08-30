# -*- coding: utf-8 -*-
import os
import html2text
import codecs

# Création list des fichiers
def list_files(path):
    files = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            files.append(name)
    return files

# Tester les fichiers
def read_files(path, file_name):
    h = html2text.HTML2Text()
    h.ignore_links = True
    contenu = codecs.open(path + file_name,'r',encoding='utf-8').read()
    return h.handle(contenu)

# Sortir des fichiers résultats
def result_files(languages):
    for langue in languages:
        path = "./resultats/HTML2text/%s/"%langue
        files_path = "./source/%s/html/"%langue
        if not os.path.exists(path):
            os.makedirs(path)
        files_names = list_files(files_path)
        for file in files_names:
          output_english_files = open(path + file, "w+")
          try:
              output_english_files.write(read_files(files_path,file).encode("utf-8","replace"))
          except:
              "UnicodeDecodeError: 'utf8' codec can't decode byte 0xcf in position 492: invalid continuation byte"

langues = ["en","el","pl","ru","zh"]
result_files(langues)