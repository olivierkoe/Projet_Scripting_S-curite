#!/bin/bash

# Vérifier si une adresse IP est fournie en argument
if [ -z "$1" ]; then
    echo "Utilisation : $0 <adresse_ip>"
    exit 1
fi

# Définir un nom de fichier de sortie
output_file="rapports/ports_scan_results.log"

# Générer un horodatage pour l'en-tête
timestamp=$(date +"%Y%m%d_%H%M%S")
header="Scan des ports ouverts sur $1 effectué le $timestamp"
separator="--------------------------------------------------"

# Lancer le scan avec nmap et capturer les résultats dans une variable
scan_result=$(nmap -Pn -sV "$1")

# Lire le contenu actuel du fichier de sortie (s'il existe)
if [ -f "$output_file" ]; then
    existing_content=$(cat "$output_file")
else
    existing_content=""
fi

# Ajouter l'en-tête et les résultats du scan au début du fichier
{
    echo "$header"
    echo "$separator"
    echo "$scan_result"
    echo "$separator"
    echo "$existing_content"
} > "$output_file"

# Afficher les résultats
echo "Résultats enregistrés dans $output_file"
cat "$output_file"
