#!/bin/bash

echo "🔍 Vérification des mots de passe faibles..."

# Vérification des mots de passe faibles avec John the Ripper
john --show /etc/shadow > rapports/weak_passwords.txt

echo "✅ Résultats enregistrés dans weak_passwords.txt"
