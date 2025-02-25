# Projet Scripting Sécurité  

## Groupe 1 (Nabiya CHERGUI & Olivier KOENIG) 

Ce projet vise à automatiser et sécuriser plusieurs aspects d'un système à l'aide de scripts en Bash et Python. Les fonctionnalités incluent : 

* 🔍 Scan des ports et services ouverts 

* 🔑 Gestion et sauvegarde des mots de passe 

* 📜 Surveillance et analyse des logs de sécurité 

* 🛡️ Automatisation des tâches de sécurité avec cron 


## 📂 Arborescence du Projet

```
Projet_Scripting_S-curite/ 
│── rapports/                          # Dossier contenant les rapports générés 
│   │── analyse_logs_report.txt        # Rapport d'analyse des logs 
│   │── Bash_scan_result_xxx.txt       # Résultats du scan avec Bash 
│   │── Python_scan_result_xxx.txt     # Résultats du scan avec Python 
│ 
│── scripts_logs/                      # Scripts pour la surveillance des logs 
│   │── analyse_logs.py                # Analyse des logs en Python 
│   │── surveillance_logs.sh           # Surveillance en temps réel avec Bash 
│   │── README_logs.md                 # Documentation spécifique à l'analyse des logs 
│ 
│── scripts_pwd/                       # Scripts pour la gestion des mots de passe 
│   │── backups/                       # Dossier contenant les sauvegardes 
│   │   │── passwords_backup_xxx.enc   # Sauvegardes horodatées 
│   │── secrets/                       # Dossier contenant les fichiers sécurisés 
│   │   │── key.key                    # Clé de chiffrement 
│   │   │── passwords.enc              # Mots de passe chiffrés 
│   │── backup_passwords.sh            # Script Bash pour sauvegarde auto 
│   │── password_manager.py            # Script Python pour gestion des mots de passe 
│   │── README_pwd.md                  # Documentation spécifique à la gestion des mots de passe 
│ 
│── scripts_scan/                      # Scripts pour le scan des ports et services 
│   │── analyse_scan.py                # Scan des ports en Python 
│   │── scan_ports.sh                  # Scan des ports en Bash 
│   │── README_scan.md                 # Documentation spécifique aux scans de ports 
│ 
│── venv/                              # Environnement virtuel Python 
│ 
│── README.md                          # README principal du projet 
│── requirements.txt                   # Liste des dépendances (Cryptography) 
 ```

 

 

## 📌 Installation et Configuration 

## 1️⃣ Installation des dépendances 

Sur une machine Linux, exécutez la commande suivante pour installer les outils nécessaires : 

sudo apt update && sudo apt install -y nmap net-tools python3 python3-pip git fail2ban cron hydra 

 

## 2️⃣ Clonage du dépôt 

git clone https://github.com/olivierkoe/Projet_Scripting_S-curite.git 
cd Projet_Scripting_S-curite 

 
 

## 3️⃣ Création d'un environnement virtuel (venv) 

Nous avons utilisé un environnement virtuel Python (venv) pour isoler les dépendances du projet. Cela permet d'éviter les conflits entre les packages installés globalement sur le système. 

python -m venv venv 
source venv/bin/activate  # Activation du venv  
 

Ensuite, nous avns installer les dépendances du projet : 

pip install -r requirements.txt 
 

📌 Pourquoi utiliser un venv ? 

* Évite les conflits entre les versions des bibliothèques. 

* Facilite la portabilité du projet sur différentes machines. 

* Permet d’assurer que les versions utilisées sont bien définies dans requirements.txt. 

 

## 4️⃣ Création des dossiers et arborescence 

mkdir -p scripts_scan scripts_pwd scripts_logs rapports  

 

Pour mieux organiser la documentation, nous avons également créé un README général et des fichiers README spécifiques pour chaque module : 

touch README.md                           # README général du projet  

touch scripts_scan/README_scan.md 
touch scripts_pwd/README_pwd.md 
touch scripts_logs/README_logs.md 
touch README_cron.md          # Pour l'automatisation avec cron 

 

## 5️⃣ Répartition des tâches

Dans ce projet, nous avons réparti les tâches de manière **équilibrée et collaborative**.

| Tâche                                      | Responsable      |
|-------------------------------------------|-----------------|
| Scan des ports et services ouverts     | Olivier         |
| Gestion sécurisée des mots de passe    | Nabiya          |
| Analyse et surveillance des logs       | Nabiya          |
| Automatisation des sauvegardes et sécurité | Olivier     |
| Rédaction des README pour la doc       | Binôme          |
| Création du PowerPoint                 | Binôme (chacun a rédigé sa partie) |
| Tests et validation des scripts         | Binôme          |
| Organisation du dépôt GitHub            | Binôme          |
| Finalisation et revue du projet        | Binôme          |

---

### 🏗️ Méthodologie de travail :

- Chacun a pris en charge les scripts qu'il devait développer.**  
- La documentation et les tests ont été faits en binôme** pour assurer une meilleure qualité et une bonne compréhension mutuelle.  
- L'organisation du dépôt GitHub et la mise en place des fichiers README ont été faites ensemble.**  
- Le PowerPoint a été conçu de manière collaborative,** en intégrant les explications de chaque partie.  
 

 

 
 
## Utilisation des scripts 

**1 - Scan des ports et services ouverts**

Bash : 

./scripts_scan/scan_ports.sh <adresse_ip> 
 

Python : 

python3 scripts_scan/analyse_scan.py <adresse_ip> 
 

*Résultat* : Les résultats seront enregistrés dans rapports/ sous la forme d’un fichier .txt. 

 

**2 - Gestion des mots de passe** 

Ajouter un mot de passe : 

python3 scripts_pwd/password_manager.py 
 

➡️ Sélectionnez "1. Ajouter un mot de passe", puis entrez : 

Nom du site 

Identifiant 

Mot de passe 

Récupérer un mot de passe : 

python3 scripts_pwd/password_manager.py 
 

➡️ Sélectionnez "2. Récupérer un mot de passe" et entrez le site voulu. 

💾 Sauvegarde automatique : Un script Bash permet de sauvegarder la base de données chiffrée des mots de passe : 

./scripts_pwd/backup_passwords.sh 
 

Les sauvegardes sont stockées dans scripts_pwd/backups/. 

 

**3 - Surveillance et analyse des logs de sécurité** 

Surveillance en temps réel des échecs de connexion : 

 

./scripts_logs/surveillance_logs.sh 
 

Analyse des logs pour détecter les attaques : 

python3 scripts_logs/analyse_logs.py 
 

📌 Rapport généré : rapports/analyse_logs_report.txt 

 

**4 - Automatisation avec cron** 

Les tâches critiques sont automatisées avec cron : 

crontab -e 
 

Ajoutez cette ligne pour une sauvegarde automatique des mots de passe chaque jour à 3h du matin : 

0 3 * * * /bin/bash /chemin/vers/scripts_pwd/backup_passwords.sh 
 

 

## Conclusion 

Ce projet fournit des outils essentiels pour : 

Améliorer la sécurité du système. 

Automatiser des tâches critiques. 

Détecter les intrusions et attaques potentielles. 

## Possibles améliorations : 

- Ajouter un système d’alerte en cas de détection d’attaque. 

- Intégrer une notification par email pour certaines alertes. 