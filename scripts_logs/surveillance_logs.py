#!/usr/bin/env python3


import subprocess

log_file = "/var/log/auth.log"
print(f"🔍 Surveillance en temps réel des échecs de connexion dans {log_file}")

try:
    process = subprocess.Popen(
        ["sudo", "tail", "-f", log_file],
        stdout=subprocess.PIPE,
        text=True
    )
    for line in process.stdout:
        if "Failed password" in line or "Invalid user" in line or "authentication failure" in line:
            print(f"⚠️ Tentative de connexion échouée : {line.strip()}")
except KeyboardInterrupt:
    print("\n🛑 Arrêt de la surveillance.")
except Exception as e:
    print(f"❌ Erreur : {e}")
