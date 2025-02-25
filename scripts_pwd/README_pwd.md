# 🔑 Gestion sécurisée des mots de passe

## Explication du comportement et des résultats

### 🔹 Objectif global

L'objectif de cette partie est de permettre aux utilisateurs de stocker leurs mots de passe de manière sécurisée en utilisant un gestionnaire de mots de passe en Python tout en assurant une politique de robustesse des mots de passe.  
En complément, un script Bash est utilisé pour automatiser la sauvegarde de ces mots de passe afin d'éviter toute perte de données.  

---

### 🔹 Fonctionnement du script Python (`password_manager.py`)

#### 📌 Génération et gestion d'une clé de chiffrement :
- Une clé unique est générée et stockée dans `secrets/key.key`.
- Cette clé est utilisée pour chiffrer et déchiffrer les mots de passe.

#### 📌 Ajout d'un mot de passe sécurisé :
1. L'utilisateur choisit un site, un identifiant, et un mot de passe.
2. Avant l'enregistrement, une vérification de la robustesse est effectuée :
   - ✅ Min. **8 caractères**
   - ✅ Au moins **1 majuscule**
   - ✅ Au moins **1 minuscule**
   - ✅ Au moins **1 chiffre**
   - ✅ Au moins **1 symbole spécial**
3. Si le mot de passe est trop faible, l'utilisateur doit en choisir un autre.
4. Une fois accepté, le mot de passe est **chiffré et stocké** dans `passwords.enc`.

#### 📌 Récupération d'un mot de passe :
1. L'utilisateur saisit le nom du site pour lequel il veut récupérer ses identifiants.
2. Le programme **déchiffre les données** et affiche l’identifiant et le mot de passe associés.

#### 🔹 Résultat attendu :
Si l'utilisateur entre un mot de passe conforme aux règles, il est accepté et enregistré.  
Sinon, il est rejeté et l'utilisateur doit le modifier.  

---

### 🔹 Fonctionnement du script Bash (`backup_passwords.sh`)

#### 📌 Création des dossiers nécessaires :
- Vérifie si le dossier `scripts_pwd/backups` existe.
- Si ce n'est pas le cas, il est créé automatiquement.

#### 📌 Sauvegarde du fichier de mots de passe (`passwords.enc`) :
1. Vérifie si le fichier `passwords.enc` existe.
2. Si oui, il est **copié avec un horodatage** dans `scripts_pwd/backups/` sous le format : passwords_backup_YYYYMMDD_HHMMSS.enc
3. Si non, un message indique qu'il n'y a **aucun fichier à sauvegarder**.

#### 🔹 Résultat attendu :
Si `passwords.enc` existe → une sauvegarde est créée et un message de succès s'affiche.  
Sinon, un message indique que le fichier est introuvable.  

---

## 📌 Explication des résultats observés lors des tests

### 🔹 Exécution du gestionnaire de mots de passe (`password_manager.py`)
- Si l’utilisateur tente d’entrer un mot de passe trop faible, **il est rejeté**.
- Une fois un mot de passe robuste validé, **il est stocké de manière chiffrée**.
- Un test de récupération du mot de passe permet de confirmer que **les identifiants enregistrés sont bien accessibles après déchiffrement**.

### 🔹 Exécution du script de sauvegarde (`backup_passwords.sh`)
- Après avoir ajouté des mots de passe, un **test de sauvegarde automatique** est effectué.
- Un fichier chiffré est **correctement stocké** dans le dossier `backups` avec un **horodatage unique**.
- Si `passwords.enc` est **supprimé avant l'exécution** du script, le message **"Aucun fichier de mots de passe trouvé."** s'affiche.

---

## 📌 Conclusion et pertinence par rapport à la politique de sécurité

### ✅ Politique de robustesse des mots de passe
✔️ Évite l'utilisation de mots de passe trop faibles grâce aux règles imposées.  
✔️ Permet une **sécurisation maximale des identifiants** via le chiffrement.

### ✅ Automatisation et protection des données
✔️ La **sauvegarde automatique** permet d'éviter toute perte accidentelle de mots de passe.  
✔️ L'horodatage assure une **gestion des versions** et permet de revenir à une sauvegarde antérieure en cas de besoin.

### **Conclusion**
➡️ Grâce à ces deux scripts, nous mettons en place **une solution complète** de gestion et de protection des mots de passe, conforme aux **bonnes pratiques de cybersécurité**. 

