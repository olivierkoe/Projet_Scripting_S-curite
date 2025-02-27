#!/usr/bin/env python3

import os
import json
import re
import getpass  # 🛠️ Ajout de l'import pour `getpass`
from cryptography.fernet import Fernet

# 📂 Dossiers pour les fichiers sécurisés
secrets_dir = "scripts_pwd/secrets"
passwords_file = f"{secrets_dir}/passwords.enc"
key_file = f"{secrets_dir}/key.key"

# 🔧 Vérifie si le dossier existe, sinon le crée
os.makedirs(secrets_dir, exist_ok=True)

# 🔑 Charger ou générer une clé de chiffrement
def load_or_generate_key():
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, "wb") as f:
            f.write(key)
        print("🔑 Nouvelle clé générée.")
    else:
        with open(key_file, "rb") as f:
            key = f.read()
    return key  # 🛠️ Retourne la clé brute, pas l'objet Fernet

# 🔒 Chiffrement et déchiffrement
def encrypt_data(data, cipher):
    return cipher.encrypt(data.encode()).decode()

def decrypt_data(data, cipher):
    return cipher.decrypt(data.encode()).decode()

# 📂 Charger ou initialiser la base de mots de passe
def load_passwords(cipher):
    if os.path.exists(passwords_file):
        with open(passwords_file, "rb") as f:
            encrypted_data = f.read()
        try:
            return json.loads(decrypt_data(encrypted_data.decode(), cipher))
        except:
            print("⚠️ Erreur de déchiffrement ! Mauvaise clé ?")
            return {}
    return {}

def save_passwords(data, cipher):
    encrypted_data = encrypt_data(json.dumps(data), cipher)
    with open(passwords_file, "wb") as f:
        f.write(encrypted_data.encode())

# ✅ Vérification de la robustesse du mot de passe
def check_password_strength(password):
    """ Vérifie si un mot de passe est robuste """
    if len(password) < 8:
        return "❌ Trop court (min. 8 caractères)."
    if not re.search(r"[A-Z]", password):
        return "❌ Il manque une MAJUSCULE."
    if not re.search(r"[a-z]", password):
        return "❌ Il manque une MINUSCULE."
    if not re.search(r"\d", password):
        return "❌ Il manque un CHIFFRE."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "❌ Il manque un SYMBOLE (!@#$%^&*...)."
    
    return "✅ Mot de passe robuste."

# 🔐 Ajouter un mot de passe après vérification
def add_password(site, username, password, cipher):
    passwords = load_passwords(cipher)
    passwords[site] = {"username": username, "password": password}
    save_passwords(passwords, cipher)
    print(f"✅ Mot de passe sécurisé enregistré pour {site}.")

# 🔓 Récupérer un mot de passe
def get_password(site):
    # 🔑 Demande la clé à l'utilisateur au moment du déchiffrement
    user_key = getpass.getpass("🔐 Entrez votre clé de chiffrement pour récupérer le mot de passe : ").encode()

    try:
        cipher = Fernet(user_key)  # Vérifie si la clé est correcte
        passwords = load_passwords(cipher)

        if site in passwords:
            print(f"🔑 Identifiant : {passwords[site]['username']}")
            print(f"🔒 Mot de passe : {passwords[site]['password']}")
        else:
            print("❌ Aucun mot de passe trouvé pour ce site.")
    
    except:
        print("❌ Clé invalide. Impossible de récupérer le mot de passe.")

# 🔽 Interface utilisateur
def main():
    print("\n🔐 Gestionnaire de mots de passe")
    print("1. Ajouter un mot de passe")
    print("2. Récupérer un mot de passe")
    choix = input("➡️ Choisissez une option : ")

    if choix == "1":
        site = input("🌐 Site : ")
        username = input("👤 Identifiant : ")

        # 🔑 Charge la clé de chiffrement avant d'ajouter un mot de passe
        key = load_or_generate_key()
        cipher = Fernet(key)

        # 🔄 Demander un mot de passe robuste
        print("\n🔒 **Règles du mot de passe sécurisé** :")
        print(" - Min. **8 caractères**")
        print(" - Min. **1 majuscule** (A-Z)")
        print(" - Min. **1 minuscule** (a-z)")
        print(" - Min. **1 chiffre** (0-9)")
        print(" - Min. **1 symbole spécial** (!@#$%^&*...)")
        print("------------------------------------------------\n")

        while True:
            password = input("🔑 Mot de passe : ")
            strength = check_password_strength(password)
            if "❌" not in strength:
                break
            else:
                print(f"⚠️ {strength} Réessayez !\n")

        add_password(site, username, password, cipher)

    elif choix == "2":
        site = input("🌐 Site : ")
        get_password(site)  # 🔑 La clé sera demandée dans `get_password()`

    else:
        print("❌ Choix invalide.")

if __name__ == "__main__":
    main()
