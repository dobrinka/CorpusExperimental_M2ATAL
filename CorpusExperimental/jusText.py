# coding:utf-8
import os
import justext
import codecs

# Création list des fichiers

def list_files(path):
    files = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            files.append(name)
    return files

# Tester les fichiers

def read_files(path,file_name,langue):
  contenu = codecs.open(path + file_name,'r',encoding='utf-8').read()
  paragraphs = justext.justext(contenu, justext.get_stoplist(langue))
  chaine = ""
  for paragraph in paragraphs:
    if not paragraph.is_boilerplate:
      chaine+= paragraph.text+"\n"
  print "%s\t%s"%(str(len(chaine)),file_name)
  return chaine


# Sortir des fichiers résultats

langues = {'en': 'English', 'el':'Greek', 'pl':'Polish', 'ru':"Russian"}

for init, langue in langues.items():
    path = "./resultats/jusText/%s/"%init
    files_path = "./source/%s/html/"%init
    if not os.path.exists(path):
        os.makedirs(path)

    files_names = list_files(files_path)

    for file in files_names:
      output_english_files = open(path + file, "w+")
      try:
        output_english_files.write(read_files(files_path,file,langue).encode("utf-8","replace"))
      except:
        print "Problème avec le fichier!"