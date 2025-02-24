import sys
import hashlib
import json
import smtplib
from email.mime.text import MIMEText

# Fichier pour l'historique des modifications
HISTORY_FILE = "hash_history.json"

def load_hashes(file_path):
    """Charge les hachages depuis un fichier."""
    hashes = {}
    try:
        with open(file_path, "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 2:
                    hashes[parts[1]] = parts[0]
    except FileNotFoundError:
        pass
    return hashes

def send_alert(changes):
    """Envoie un email en cas de modifications détectées."""
    sender_email = "alert@example.com"
    recipient_email = "admin@example.com"
    subject = "Alerte : Fichiers sensibles modifiés !"
    body = "Les fichiers suivants ont été modifiés :\n\n" + "\n".join(changes)

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login("alert@example.com", "password")
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print("[✔] Alerte email envoyée !")
    except Exception as e:
        print(f"[✖] Échec de l'envoi de l'email : {e}")

def save_history(history):
    """Sauvegarde l'historique des modifications dans un fichier JSON."""
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 analyze_changes.py <old_hash_file> <new_hash_file>")
        sys.exit(1)

    old_hashes = load_hashes(sys.argv[1])
    new_hashes = load_hashes(sys.argv[2])
    
    changes = []

    for file, new_hash in new_hashes.items():
        old_hash = old_hashes.get(file)
        if old_hash and old_hash != new_hash:
            changes.append(file)

    if changes:
        print("[⚠] Modifications détectées :")
        for change in changes:
            print(f" - {change}")

        send_alert(changes)

        # Charger l'historique précédent
        try:
            with open(HISTORY_FILE, "r") as f:
                history = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            history = {}

        for change in changes:
            history[change] = new_hashes[change]

        save_history(history)
    else:
        print("[✔] Aucun changement détecté.")

if __name__ == "__main__":
    main()
