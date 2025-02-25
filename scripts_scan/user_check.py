import subprocess

users_to_check = ["user1", "user2", "user3"]

for user in users_to_check:
    try:
        result = subprocess.run(["/usr/bin/lastlog", "-u", user], capture_output=True, text=True, check=True)
        if "Never logged in" in result.stdout:
            print(f"⚠️ L'utilisateur {user} n'a jamais été utilisé !")
    except FileNotFoundError:
        print("❌ La commande 'lastlog' est introuvable ! Vérifie son installation.")
    except subprocess.CalledProcessError:
        print(f"⚠️ Problème lors de l'exécution de lastlog pour {user}.")
