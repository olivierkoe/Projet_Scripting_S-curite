#!/usr/bin/python3

import hashlib
import os

# Définir le chemin du fichier log où les résultats des vérifications seront enregistrés
LOG_FILE = "./rapports/ports_scan_results.log"

# Vérifier si le dossier "rapports" existe, sinon le créer
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# Fichier contenant la liste des fichiers à surveiller
MONITORED_FILES = "./config/monitored_files.txt"

def check_file_integrity(file_path):
    """Calcule le hash SHA256 d'un fichier pour vérifier son intégrité."""
    try:
        print(f"Vérification du fichier : {file_path}")  # Affiche un message de débogage
        with open(file_path, 'rb') as f:
            # Calculer et retourner le hash SHA256 du fichier
            return hashlib.sha256(f.read()).hexdigest()
    except FileNotFoundError:
        # En cas de fichier introuvable, afficher un message d'erreur et retourner None
        print(f"[!] Fichier introuvable : {file_path}")
        return None

def load_previous_hashes():
    """Charge les hachages précédents à partir du fichier log existant."""
    previous_hashes = {}
    if os.path.exists(LOG_FILE):
        # Lire le fichier log pour récupérer les hachages des fichiers précédemment surveillés
        with open(LOG_FILE, "r") as logs:
            for line in logs:
                parts = line.strip().split()
                if len(parts) == 2:
                    # Ajouter chaque fichier et son hash dans un dictionnaire
                    previous_hashes[parts[0]] = parts[1]
    return previous_hashes

def update_log(new_hashes, previous_hashes):
    """Met à jour le fichier log avec les nouveaux hachages et les modifications détectées."""
    # Créer un fichier temporaire pour y écrire les nouvelles informations
    temp_file = LOG_FILE + ".tmp"
    
    with open(temp_file, "w") as log:
        # Ajouter les nouvelles informations en début de fichier
        for file, new_hash in new_hashes.items():
            old_hash = previous_hashes.get(file)
            if old_hash and old_hash != new_hash:
                # Si le fichier a changé, signaler le changement et l'ajouter au log
                print(f"⚠️ Changement détecté dans {file} !")
                log.write(f"⚠️ Changement détecté dans {file.upper()} : {new_hash.upper()}\n")
            else:
                # Si le fichier n'a pas changé, l'indiquer clairement
                log.write(f"✔️ Aucun changement détecté pour {file.upper()}\n")
        
        # Ajouter le reste du fichier log d'origine sans modifications
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as old_log:
                log.write(old_log.read())

    # Remplacer le fichier log par le fichier temporaire mis à jour
    os.replace(temp_file, LOG_FILE)

def analyze_changes():
    """Compare les hachages actuels avec ceux enregistrés et met à jour le log en conséquence."""
    print("Début de l'analyse des fichiers...")  # Affiche un message de débogage
    previous_hashes = load_previous_hashes()  # Charger les hachages précédents
    new_hashes = {}

    # Vérifier si le fichier contenant la liste des fichiers à surveiller existe
    if not os.path.exists(MONITORED_FILES):
        print(f"[!] Le fichier {MONITORED_FILES} est introuvable.")  # Message d'erreur si le fichier est manquant
        return

    # Lire la liste des fichiers à surveiller et vérifier leur intégrité
    with open(MONITORED_FILES, "r") as f:
        for file in f:
            file = file.strip()  # Retirer les espaces ou nouvelles lignes
            if file:
                print(f"Vérification de {file}...")  # Afficher un message pour chaque fichier vérifié
                new_hash = check_file_integrity(file)  # Vérifier l'intégrité du fichier
                if new_hash:
                    new_hashes[file] = new_hash  # Ajouter le nouveau hash au dictionnaire

    if not new_hashes:
        print("[!] Aucun changement détecté.")  # Avertir si aucun fichier n'a été modifié

    # Mettre à jour le fichier log avec les nouveaux résultats
    update_log(new_hashes, previous_hashes)

if __name__ == "__main__":
    # Lancer l'analyse des changements
    analyze_changes()
