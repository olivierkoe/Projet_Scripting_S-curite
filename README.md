
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



Exemple d'utilisation :  
🌐 Site : gmail.com  
👤 Identifiant : monemail@gmail.com  
🔒 Mot de passe : MonSuperMotDePasse123!  

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

 

**4 - Automatisation des tâches de sécurité avec cron**   
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

0 2 * * * bash ~/Projet_Scripting_Securite/scripts_scan/scan_ports.sh 192.168.1.1  

🕒 Exécuté tous les jours à 02h00   
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

0 2 * * * bash ~/Projet_Scripting_Securite/scripts_logs/surveillance_logs.sh  

🕒 Exécuté tous les jours à 02h00  
📌 Objectif : Lancer un processus de surveillance continue des logs pour détecter en temps réel des événements de sécurité (échecs de connexion, attaques brute-force, etc.).  
🔧 Script utilisé : surveillance_logs.sh  
⚡ Exécution : Utilise bash.  

5️⃣ Sauvegarde des mots de passe  

0 2 * * * bash ~/Projet_Scripting_Securite/scripts_pwd/backup-passwords.sh  

🕒 Exécuté tous les jours à 02h00  
📌 Objectif : Sauvegarder une base de données ou un fichier contenant les mots de passe stockés de manière sécurisée.  
🔧 Script utilisé : backup-passwords.sh  
⚡ Exécution : Utilise bash.  

6️⃣ Gestionnaire de mots de passe  

30 8 * * * python3 ~/Projet_Scripting_Securite/scripts_pwd/password_manager.py  

🕒 Exécuté tous les jours à 08h30  
📌 Objectif : Vérifier, gérer ou mettre à jour les mots de passe enregistrés. Il peut inclure des alertes pour des mots de passe faibles ou compromis.  
🔧 Script utilisé : password_manager.py  
⚡ Exécution : Utilise python3.  

📌 En résumé :    

🕒 Heure    📌 Tâche   

02:00       Scan des ports sur 192.168.1.1  

08:30       Analyse des scans pour détecter des anomalies  

08:30       Analyse des logs pour repérer des attaques  

02:00       Surveillance des logs en temps réel  

02:00       Sauvegarde des mots de passe  

08:30       Gestion des mots de passe



## Conclusion 

Ce projet fournit des outils essentiels pour : 

Améliorer la sécurité du système. 

Automatiser des tâches critiques. 

Détecter les intrusions et attaques potentielles. 

## Possibles améliorations : 

- Ajouter un système d’alerte en cas de détection d’attaque. 

- Intégrer une notification par email pour certaines alertes. 


