#!/bin/bash
 
# Vérifier si une adresse IP est fournie en argument
if [ -z "$1" ]; then
    echo "Utilisation : $0 <adresse_ip>"
    exit 1
fi
 
# Définir un nom de fichier unique avec un horodatage
timestamp=$(date +"%Y%m%d_%H%M%S")
output_file="rapports/Bash_scan_result_${1//./_}_$timestamp.txt"
 
# Lancer le scan avec nmap
echo "Scan des ports ouverts sur $1..."
nmap -Pn -sV "$1" > "$output_file"
 
# Afficher les résultats
echo "Résultats enregistrés dans $output_file"
cat "$output_file"
 
 