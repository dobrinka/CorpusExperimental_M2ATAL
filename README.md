# CorpusExperimental_M2ATAL
Nettoyage du corpus:

Pour extraire la partie purement textuelle des documents:
/creation des dossiers pour tous les languages avec les fichiers nettoies/ 
avec HTML2text: python HTML2text.py

/creation des dossiers pour tous les languages, avec les fichiers nettoies/ 
(seuf chinois "zh", parce qu'il y a un problème)
avec jusText: python jusText.py

L'évaluation : Qualité du nettoyage:

python RunResults.py

Pour les résultats globales(cleaneval.py):

Ce fichier créé un dossier "GlobalStatisticResults" pour chaque les utils HTML2text et jusText. Dedans il y a des dossiers et fichiers 
pour chaque langues avec des résultats globales qui sont extrait avec le script cleaneval.py

Pour les résultats locales(test_api.py):

Ce fichier créé un dossier "LocalStatisticResults" dans le dossier "resultats". Dedans il y a des dossiers et fichiers 
pour chaque langues avec des résultats locales qui sont extrait avec le script test_api.py
