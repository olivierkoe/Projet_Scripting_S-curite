#!/usr/bin/env python3

import sys
import subprocess
import datetime
import re

# Vérifier si une adresse IP ou un domaine est fourni
if len(sys.argv) < 2:
    print("Erreur : Donne une adresse IP ou un site web !")
    print("Exemple : python3 scan_ports.py 192.168.1.1")
    sys.exit(1)

cible = sys.argv[1]

# Générer un nom de fichier unique avec la date et l'heure
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"rapports/Python_scan_result_{cible.replace('.', '_')}_{timestamp}.txt"

print(f"🔍 Scan des ports ouverts sur : {cible}...")
print("⏳ Patientez, le scan peut prendre quelques instants...")

# Lancer nmap pour détecter les services
try:
    result = subprocess.run(
        ["nmap", "-Pn", "-sV", cible],
        capture_output=True, text=True, check=True
    )

    # Sauvegarder les résultats dans un fichier
    with open(output_file, "w") as f:
        f.write(result.stdout)

    print(f"✅ Scan terminé ! Résultats enregistrés dans : {output_file}")
    print(result.stdout)  # Afficher aussi les résultats dans le terminal

except FileNotFoundError:
    print("❌ Erreur : nmap n'est pas installé. Installe-le avec : sudo apt install nmap")
    sys.exit(1)

except subprocess.CalledProcessError as e:
    print("❌ Une erreur est survenue lors de l'exécution de nmap.")
    print(e)
    sys.exit(1)

# 📌 Liste des services vulnérables connus
vulnerable_services = {
    "vsftpd 2.3.4": "Faille backdoor critique",
    "OpenSSH 7.2p2": "Vulnérabilité CVE-2016-0777",
    "Apache 2.4.49": "Faille RCE CVE-2021-41773"
}

# 🔎 Analyse des résultats pour trouver des services vulnérables
alertes = []
with open(output_file, "r") as f:
    contenu = f.read()
    for service, faille in vulnerable_services.items():
        if service in contenu:
            alertes.append(f"🚨 ALERTE : {service} détecté ! ({faille})")

# Afficher les alertes
if alertes:
    print("\n⚠️  Services vulnérables détectés :")
    print("\n".join(alertes))
else:
    print("\n✅ Aucun service vulnérable détecté.")
