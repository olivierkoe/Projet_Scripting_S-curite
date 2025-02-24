#!/bin/bash

# Liste des fichiers sensibles à surveiller
FILES_TO_WATCH=("/etc/passwd" "/etc/shadow" "/etc/hosts")

HASH_FILE="hashes.txt"
TMP_HASH_FILE="hashes_new.txt"

# Vérifie si le fichier de hachages existe, sinon le crée
if [[ ! -f "$HASH_FILE" ]]; then
    echo "Initialisation du fichier de hachages..."
    for file in "${FILES_TO_WATCH[@]}"; do
        sudo sha256sum "$file" >> "$HASH_FILE"
    done
fi

# Génère un fichier temporaire avec les nouveaux hachages
> "$TMP_HASH_FILE"
for file in "${FILES_TO_WATCH[@]}"; do
    sudo sha256sum "$file" >> "$TMP_HASH_FILE"
done

# Exécute le script Python pour analyser les changements
python3 analyze_changes.py "$HASH_FILE" "$TMP_HASH_FILE"

# Mise à jour du fichier de hachages
mv "$TMP_HASH_FILE" "$HASH_FILE"
