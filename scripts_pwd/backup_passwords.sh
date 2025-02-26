#!/bin/bash

# Dossiers secrets et backups
secrets_dir="scripts_pwd/secrets"
backup_dir="scripts_pwd/backups"

# Vérifier si les dossiers existent, sinon les créer
mkdir -p "$backup_dir"

# Nom du fichier de sauvegarde avec horodatage
timestamp=$(date +"%Y%m%d_%H%M%S")
backup_file="$backup_dir/passwords_backup_$timestamp.enc"

# Vérifier si le fichier à sauvegarder existe
if [ -f "$secrets_dir/passwords.enc" ]; then
    cp "$secrets_dir/passwords.enc" "$backup_file"
    echo "✅ Sauvegarde réalisée : $backup_file"
else
    echo "❌ Aucun fichier de mots de passe trouvé."
fi