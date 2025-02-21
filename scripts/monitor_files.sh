#!/bin/bash

FILES_TO_MONITOR="config/monitored_files.txt"
LOG_FILE="rapports/ports_scan_results.log"

# Ajouter un en-tête et les nouvelles données au début du fichier log
{
    echo "Scan effectué le $(date)"
    echo "--------------------------------------------------"
    
    # Parcourir chaque fichier mentionné dans le fichier de surveillance
    for FILE in $(cat $FILES_TO_MONITOR); do
        if [ -f "$FILE" ]; then
            # Calculer le hash SHA256 du fichier et l'ajouter au début du fichier log
            sha256sum "$FILE"
        fi
    done

    # Ajouter le contenu existant du fichier log après les nouvelles données
    cat "$LOG_FILE"
} > "$LOG_FILE.tmp" && mv "$LOG_FILE.tmp" "$LOG_FILE"

# Afficher un message indiquant que les résultats ont été ajoutés au début du fichier log
echo "Les résultats ont été ajoutés au début de $LOG_FILE"
