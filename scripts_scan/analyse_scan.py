#!/usr/bin/env python3

import sys
import subprocess
import datetime
import os
import re

# Vérifier si une adresse IP ou un domaine est fourni
if len(sys.argv) < 2:
    print("Erreur : Donne une adresse IP ou un site web !")
    print("Exemple : python3 scan_ports.py 192.168.1.1")
    sys.exit(1)

# Récupérer l'adresse à scanner
cible = sys.argv[1]

# Générer un nom de fichier unique avec la date et l'heure
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = "rapports/ports_scan_results.log"

# Créer un message d'en-tête pour l'ajouter au début du fichier
header = f"\n\nScan des ports ouverts sur : {cible} effectué le {timestamp}\n{'-'*50}\n"

print(f" Scan des ports ouverts sur : {cible}...")
print(" Patientez, le scan peut prendre quelques instants...")

# Lancer nmap via Python (comme dans le script Bash)
try:
    result = subprocess.run(
        ["nmap", "-Pn", "-sV", cible],  # Commande équivalente à Bash
        capture_output=True, text=True, check=True
    )

    # Lire le contenu actuel du fichier, si il existe
    if os.path.exists(output_file):
        try:
            with open(output_file, "r") as f:
                existing_content = f.read()
        except IOError as e:
            print(f"Erreur de lecture du fichier existant : {e}")
            sys.exit(1)
    else:
        existing_content = ""  # Si le fichier n'existe pas encore, on commence avec du vide

    # Exclure l'horodatage de la comparaison
    def remove_timestamp(text):
        return re.sub(r"Scan des ports ouverts sur : .+ effectué le \d{8}_\d{6}\n", "", text)

    # Comparer les nouvelles données avec les anciennes sans les dates
    clean_result = remove_timestamp(result.stdout.strip())
    clean_existing_content = remove_timestamp(existing_content.strip())

    if clean_result == clean_existing_content:
        # Si les données sont inchangées, ajouter "données inchangées" au début du fichier
        header = "\nDonnées inchangées\n" + header
    else:
        # Sinon, ajouter les nouvelles données
        header = "\nNouvelles données détectées\n" + header

    # Ajouter l'en-tête au début du contenu existant et les résultats du scan
    try:
        with open(output_file, "w") as f:
            f.write(header + result.stdout + "\n" + existing_content)

        print(f"Scan terminé ! Résultats enregistrés dans : {output_file}")
        print(result.stdout)  # Afficher aussi les résultats dans le terminal

    except IOError as e:
        print(f"Erreur lors de l'écriture dans le fichier : {e}")
        sys.exit(1)

except FileNotFoundError:
    print("Erreur : nmap n'est pas installé. Installe-le avec : sudo apt install nmap")
    sys.exit(1)

except subprocess.CalledProcessError as e:
    print("Une erreur est survenue lors de l'exécution de nmap.")
    print(e)
    sys.exit(1)
