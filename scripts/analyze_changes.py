#!/usr/bin/python3

import hashlib
import os

LOG_FILE = "./rapports/ports_scan_results.log"

# Vérifier si le dossier "rapports" existe, sinon le créer
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

MONITORED_FILES = "./config/monitored_files.txt"

def check_file_integrity(file_path):
    """Calcule le hash SHA256 d'un fichier."""
    try:
        print(f"Vérification du fichier : {file_path}")  # Debug
        with open(file_path, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
    except FileNotFoundError:
        print(f"[!] Fichier introuvable : {file_path}")
        return None

def load_previous_hashes():
    """Charge les hachages précédents du fichier log."""
    previous_hashes = {}
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as logs:
            for line in logs:
                parts = line.strip().split()
                if len(parts) == 2:
                    previous_hashes[parts[0]] = parts[1]
    return previous_hashes

def update_log(new_hashes, previous_hashes):
    """Met à jour le fichier log en ajoutant ou modifiant les lignes existantes."""
    # Créer un fichier temporaire pour la mise à jour
    temp_file = LOG_FILE + ".tmp"
    
    with open(temp_file, "w") as log:
        # Ajouter les nouvelles informations en début de fichier
        for file, new_hash in new_hashes.items():
            old_hash = previous_hashes.get(file)
            if old_hash and old_hash != new_hash:
                print(f"⚠️ Changement détecté dans {file} !")
                # Si le fichier a changé, ajouter au début
                log.write(f"⚠️ Changement détecté dans {file.upper()} : {new_hash.upper()}\n")
            else:
                # Si le fichier n'a pas changé, ajouter un message "pas de changement"
                log.write(f"✔️ Aucun changement détecté pour {file.upper()}\n")
        
        # Ajouter le reste du fichier log d'origine sans modifications
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as old_log:
                log.write(old_log.read())

    # Remplacer le fichier log par le fichier temporaire
    os.replace(temp_file, LOG_FILE)

def analyze_changes():
    """Compare les hachages actuels avec ceux enregistrés et met à jour le log."""
    print("Début de l'analyse...")  # Debug
    previous_hashes = load_previous_hashes()
    new_hashes = {}

    if not os.path.exists(MONITORED_FILES):
        print(f"[!] Le fichier {MONITORED_FILES} est introuvable.")
        return

    with open(MONITORED_FILES, "r") as f:
        for file in f:
            file = file.strip()
            if file:
                print(f"Vérification de {file}...")  # Debug
                new_hash = check_file_integrity(file)
                if new_hash:
                    new_hashes[file] = new_hash

    if not new_hashes:
        print("[!] Aucun changement détecté.")  # Debug

    # Mettre à jour le fichier log avec les nouvelles informations
    update_log(new_hashes, previous_hashes)

if __name__ == "__main__":
    analyze_changes()
