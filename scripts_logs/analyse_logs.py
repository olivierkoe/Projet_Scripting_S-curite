#!/usr/bin/env python3

import re
import os

# Fichier de logs à analyser
log_file = "/var/log/auth.log"
output_file = "rapports/analyse_logs_report.txt"

# Vérifier si le fichier de log existe
if not os.path.exists(log_file):
    print(f"❌ Erreur : Le fichier {log_file} n'existe pas.")
    exit(1)

# Expression régulière mise à jour pour capturer IPv4 et IPv6
pattern = r"Failed password for (?:invalid user )?(\S+) from ([\d\.:a-fA-F]+) port"

# Dictionnaire pour stocker les tentatives échouées
failed_attempts = {}

# Lire et analyser les logs
with open(log_file, "r") as file:
    for line in file:
        match = re.search(pattern, line)
        if match:
            user = match.group(1)  # L’utilisateur utilisé (ou "invalid user")
            ip = match.group(2)    # L’adresse IP (IPv4 ou IPv6)
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

# Générer un rapport des IP suspectes
with open(output_file, "w") as report:
    report.write("📌 Rapport des tentatives de connexion échouées 📌\n")
    report.write("="*50 + "\n")

    if failed_attempts:
        for ip, count in failed_attempts.items():
            report.write(f"🔴 {ip} - {count} tentatives échouées\n")
    else:
        report.write("✅ Aucun échec de connexion détecté.\n")

print(f"✅ Analyse terminée. Rapport généré : {output_file}")
