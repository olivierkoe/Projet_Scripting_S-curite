#!/bin/bash

# Vérifier si une adresse IP a été fournie en argument. Si non, afficher un message d'erreur et quitter.
if [ -z "$1" ]; then
    echo "Utilisation : $0 <adresse_ip>"  # Demander l'adresse IP en argument
    exit 1  # Quitter le script avec un code d'erreur
fi

# Définir le fichier de sortie où les résultats seront enregistrés
output_file="rapports/ports_scan_results.log"

# Générer un horodatage (date et heure) pour l'en-tête du rapport
timestamp=$(date +"%Y%m%d_%H%M%S")
header="Scan des ports ouverts sur $1 effectué le $timestamp"
separator="--------------------------------------------------"  # Séparateur pour la lisibilité

# Lancer le scan des ports avec nmap sur l'adresse IP fournie, en utilisant l'option -Pn pour ignorer le test de disponibilité de l'hôte, et -sV pour détecter les versions des services.
scan_result=$(nmap -Pn -sV "$1")

# Vérifier si le fichier de sortie existe déjà et lire son contenu existant, s'il y en a
if [ -f "$output_file" ]; then
    existing_content=$(cat "$output_file")  # Lire le contenu existant du fichier
else
    existing_content=""  # Si le fichier n'existe pas, il n'y a pas de contenu précédent
fi

# Ajouter l'en-tête, les résultats du scan, et le contenu existant dans le fichier de sortie
{
    echo "$header"  # Ajouter l'en-tête avec l'IP et la date
    echo "$separator"  # Ajouter une ligne de séparation pour une meilleure lisibilité
    echo "$scan_result"  # Ajouter les résultats du scan
    echo "$separator"  # Ajouter une autre ligne de séparation
    echo "$existing_content"  # Ajouter le contenu existant si le fichier n'est pas vide
} > "$output_file"  # Rediriger le tout vers le fichier de sortie

# Afficher un message confirmant que les résultats ont été enregistrés et afficher le contenu du fichier
echo "Résultats enregistrés dans $output_file"
cat "$output_file"
