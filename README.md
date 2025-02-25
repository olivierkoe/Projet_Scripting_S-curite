# 🛡️ Projet Scripting Sécurité  

## 📌 **Groupe 1**  
👥 **Membres du projet :**    
- 🏆 **Olivier KOENIG**  
- 🏆 **Nabiya CHERGUI**  

---

## 📖 **Organisation du projet**  
📌 **Objectif** : Automatiser des tâches de sécurité avec **Python et Bash**.    
📌 **Répartition des tâches** :  

-  **Partie A** → *Surveillance des fichiers sensibles* **(Olivier)**  
-  **Partie B** → *Gestionnaire de mots de passe sécurisé* **(Nabiya) ✅ Réalisé**  
-  **Partie C** → *Détection des ports et services vulnérables* **(Réalisé ensemble ✅)**  
-  **Partie D** → *Automatisation de la gestion des utilisateurs et de la sécurité des mots de passe* **(Olivier)**   
-  **Partie E** → *Script de surveillance des logs de sécurité (auth.log)* **(Nabiya)**  
-  **Partie F** → *Automatisation des mises à jour de sécurité* **(réalisé ensemble)**  

---

## ⚙️ **Guide d’installation**  
	**Installation des outils nécessaires :**  

sudo apt update && sudo apt install -y nmap net-tools python3 python3-pip git cron hydra fail2ban 

	**Mise en place de l'environnement virtuel (`venv`)**  
Pour isoler les dépendances du projet, nous avons créé un **environnement virtuel Python (`venv`)**.  

📌 **Création de l'environnement virtuel :**  

python3 -m venv venv  

- Activation de l’environnement virtuel : source venv/bin/activate  

- Installation des dépendances requises : pip install -r requirements.txt  

- Désactiver l’environnement virtuel quand on a fini de travailler : deactivate  
 
_ Pour réactiver venv plus tard : source venv/bin/activate  



##Créer le repertoire distant sur GitHub  

Inviter les contributeurs et notre référent  

#Créer le fichier README.md  

touch README.md  

#Se connecter et cloner le dépot distant sur les machines des contributeurs :  

git clone https://github.com/ton-pseudo/Projet_Scripting_Securite.git  



##Créer les  dossiers :   

mkdir scripts_pwd scripts_scan docs rapports  

Explication :  

📁 scripts_pwd/ → Gestion et sauvegarde des mots de passe.  
📁 scripts_scan/ → Scan et analyse des ports/services ouverts.  
📁 docs/ → Documentation et fichiers annexes.  
📁 rapports/ → Stockage des résultats des analyses.  



## Partie B - Outil de gestion des mots de passe**  
**Réalisé par :** *Nabiya*  
---

#1 Création des fichiers**  
Dans cette partie, nous avons mis en place un **gestionnaire de mots de passe sécurisé**, en utilisant **Python pour la gestion et Bash pour l’automatisation**.  

 **Fichiers créés :**  
- `scripts_pwd/password_manager.py` → *Gestion et chiffrement des mots de passe (Python).*  
- `scripts_pwd/backup_passwords.sh` → *Automatisation de la sauvegarde des mots de passe (Bash).*  

---

#2 Développement du `password_manager.py`**  
Ce script permet **d’ajouter et de récupérer des mots de passe** tout en les chiffrant.   
Chiffrement des mots de passe avec cryptography  

 **Commande pour exécuter le gestionnaire :**  

python3 scripts_pwd/password_manager.py  

Lorsqu’on lance ce script, un menu interactif apparaît :  

Gestionnaire de mots de passe  
1. Ajouter un mot de passe  

2. Récupérer un mot de passe  
➡️ Choisissez une option : 

Exemple d'utilisation : 
🌐 Site : gmail.com  
👤 Identifiant : monemail@gmail.com  
🔒 Mot de passe : MonSuperMotDePasse123!  

Résultat → Le mot de passe est chiffré et stocké dans scripts_pwd/secrets/passwords.enc  


#3 Développement du `backup_passwords.sh`**  
Objectif : Automatiser la sauvegarde des mots de passe pour éviter toute perte de données.  

**Commande pour exécuter la sauvegarde manuellement :**  

bash scripts_pwd/backup_passwords.sh  


Vérifier si la sauvegarde a bien été faite :  

ls -l scripts_pwd/backups/  

=> Résultat → Un fichier passwords_backup_xxxx.enc devrait apparaître dans scripts_pwd/backups/.  


#4 Automatisation avec cron **  
Objectif : Exécuter automatiquement la sauvegarde des mots de passe chaque jour à 3h du matin.  

**Commande pour éditer la liste des tâches planifiées : **  

crontab -e  

Ajoutez cette ligne dans le fichier cron : 0 3 * * * /bin/bash /home/nabs/projet_scripting_securite/Projet_Scripting_S-curite/scripts_pwd/backup_passwords.sh  

Vérifier que cron a bien pris en compte la tâche : crontab -l  

Résultat → Si la ligne apparaît, la sauvegarde se fera automatiquement tous les jours à 3h du matin.  





## Partie C - Détection des ports et services vulnérables**  
**Réalisé par :** *Nabiya & Olivier*  

#Création des scripts  
 Les fichiers créés :  

 scripts_scan/scan_ports.sh (Bash - Scan des ports avec nmap)  
 scripts_scan/analyse_scan.py (Python - Analyse des résultats)  


#Rendre les scripts exécutables  

chmod +x scripts_scan/scan_ports.sh  
chmod +x scripts_scan/analyse_scan.py  


#Exécuter les scans   
 - Lancer un scan des ports ouverts :  

scripts_scan/scan_ports.sh <adresse_IP>  

 Exemple :   

 scripts_scan/scan_ports.sh 192.168.1.140  

 - Lancer l’analyse des résultats en Python :  

python3 scripts_scan/analyse_scan.py  

 - Les résultats sont stockés dans rapports/.  

## D. Analyser les Logs pour Détecter les Intrusions  
**Réalisé par :** *Olivier*  

Une autre tâche de sécurité consiste à analyser les fichiers de log pour identifier les signes d'une intrusion ou d'une tentative d'accès non autorisé. Le script suivant analyse les fichiers /var/log/auth.log et /var/log/syslog à la recherche de tentatives de connexion échouées.  

* * * * * commande  
│ │ │ │ │  
│ │ │ │ └── Jour de la semaine (0-7, où 0 et 7 = Dimanche)  
│ │ │ └──── Mois (1-12)  
│ │ └────── Jour du mois (1-31)  
│ └──────── Heure (0-23)  
└────────── Minute (0-59)  

1️⃣ Scan des ports  

2 0 * * * bash ~/Projet_Scripting_Securite/scripts_scan/scan_ports.sh 192.168.1.1  

🕒 Exécuté tous les jours à 00h02 (minuit + 2 minutes)  
📌 Objectif : Lancer un script de scan des ports sur l'adresse 192.168.1.1 pour identifier les ports ouverts sur ce réseau.  
🔧 Script utilisé : scan_ports.sh  
⚡ Exécution : Utilise bash pour exécuter le script.  

2️⃣ Analyse des résultats du scan  

30 8 * * * python3 ~/Projet_Scripting_Securite/scripts/analyse_scan.py    

🕒 Exécuté tous les jours à 08h30  
📌 Objectif : Analyser les résultats du scan des ports effectué à minuit. Il peut détecter des changements suspects.  
🔧 Script utilisé : analyse_scan.py  
⚡ Exécution : Utilise python3.  

3️⃣ Analyse des logs  

30 8 * * * python3 ~/Projet_Scripting_Securite/scripts_logs/analyse_logs.py  

🕒 Exécuté tous les jours à 08h30  
📌 Objectif : Analyser les journaux système (auth.log, syslog, etc.) pour repérer des anomalies comme des tentatives d'accès non autorisées.  
🔧 Script utilisé : analyse_logs.py  
⚡ Exécution : Utilise python3.  

4️⃣ Surveillance des logs en temps réel  

30 8 * * * bash ~/Projet_Scripting_Securite/scripts_logs/surveillance_logs.sh  

🕒 Exécuté tous les jours à 08h30  
📌 Objectif : Lancer un processus de surveillance continue des logs pour détecter en temps réel des événements de sécurité (échecs de connexion, attaques brute-force, etc.).  
🔧 Script utilisé : surveillance_logs.sh  
⚡ Exécution : Utilise bash.  

5️⃣ Sauvegarde des mots de passe  

30 9 * * * bash ~/Projet_Scripting_Securite/scripts_pwd/backup-passwords.sh  

🕒 Exécuté tous les jours à 09h30  
📌 Objectif : Sauvegarder une base de données ou un fichier contenant les mots de passe stockés de manière sécurisée.  
🔧 Script utilisé : backup-passwords.sh  
⚡ Exécution : Utilise bash.  

6️⃣ Gestionnaire de mots de passe  

30 9 * * * python3 ~/Projet_Scripting_Securite/scripts_pwd/password_manager.py  

🕒 Exécuté tous les jours à 09h30  
📌 Objectif : Vérifier, gérer ou mettre à jour les mots de passe enregistrés. Il peut inclure des alertes pour des mots de passe faibles ou compromis.  
🔧 Script utilisé : password_manager.py  
⚡ Exécution : Utilise python3.  

📌 En résumé :    

🕒 Heure	📌 Tâche   

00:02		Scan des ports sur 192.168.1.1  

08:30		Analyse des scans pour détecter des anomalies  

08:30		Analyse des logs pour repérer des attaques  

08:30		Surveillance des logs en temps réel  

09:30		Sauvegarde des mots de passe  

09:30		Gestion des mots de passe
