#!/bin/bash

FILES_TO_MONITOR="config/monitored_files.txt"
LOG_FILE="rapports/ports_scan_results.log"

# Vérifier si le fichier de log existe sinon le créer
if [ ! -f "$LOG_FILE" ]; then
    touch "$LOG_FILE"
fi

# Créer un fichier temporaire
TEMP_FILE=$(mktemp)

# Ajouter un en-tête indiquant l'heure du scan (facultatif mais pratique)
echo "Scan effectué le $(date)" > "$TEMP_FILE"

# Ajouter un séparateur pour distinguer chaque nouvelle exécution
echo "--------------------------------------------------" >> "$TEMP_FILE"

# Boucle à travers les fichiers à surveiller
for FILE in $(cat $FILES_TO_MONITOR); do
    if [ -f "$FILE" ]; then
        # Calculer et ajouter le hash SHA256 du fichier au log
        sha256sum "$FILE" >> "$TEMP_FILE"
    fi
done

# Ajouter le contenu du fichier log existant à la fin du fichier temporaire
cat "$LOG_FILE" >> "$TEMP_FILE"

# Remplacer le fichier de log par le fichier temporaire
mv "$TEMP_FILE" "$LOG_FILE"

echo "Les résultats ont été ajoutés à $LOG_FILE"
