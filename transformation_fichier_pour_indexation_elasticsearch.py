import json

# Fichier d'entrée contenant vos lignes JSON
input_file = "../datasets/evenements.json"  # Assurez-vous que ce fichier est dans le répertoire courant
# Fichier de sortie formaté pour Elasticsearch
output_file = "../datasets/output_bulk.json"  # Fichier généré dans le même répertoire

# Nom de l'index Elasticsearch
index_name = "evenements"

# Lecture et transformation
try:
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        # Lire tout le contenu du fichier
        raw_data = infile.read()
        
        # Transformer en une liste de documents JSON
        documents = json.loads(f"[{raw_data.replace('}{', '},{')}]")

        for idx, document in enumerate(documents):
            # Écrire la commande d'indexation
            index_line = {"index": {"_index": index_name, "_id": idx}}
            outfile.write(json.dumps(index_line) + "\n")
            
            # Écrire le document JSON
            outfile.write(json.dumps(document, ensure_ascii=False) + "\n")

    print(f"Transformation terminée. Fichier écrit : {output_file}")

except Exception as e:
    print(f"Erreur : {e}")