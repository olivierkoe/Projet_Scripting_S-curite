# 📜 Surveillance et analyse des logs de sécurité

## 🔹 Objectif global

L'objectif de cette partie est de surveiller en temps réel et analyser les logs de connexion (`auth.log`) afin de détecter les tentatives d'intrusion.  
Deux scripts sont utilisés :  
✔ **Un script Bash** pour une surveillance en direct des tentatives d’accès échouées.  
✔ **Un script Python** pour une analyse plus approfondie et la génération d’un rapport des adresses IP suspectes.  

---

## 🔹 Fonctionnement du script Bash (`monitor_auth_log.sh`)

📌 **Surveillance en temps réel des tentatives de connexion échouées.**  

- Écoute du fichier `/var/log/auth.log` en temps réel avec la commande `tail -f`.  
- Filtrage des tentatives échouées en recherchant les lignes contenant `"Failed password"`.  
- Affichage instantané des tentatives de connexion échouées sous la forme :  

```bash
⚠️ Tentative de connexion échouée : Feb 24 12:37:29 kali sshd[86892]: Failed password for root from 192.168.1.140 port 50234 ssh2
```

 ### 🔹 Résultat attendu  
✅ Lorsqu'un attaquant essaie de se connecter avec un mauvais mot de passe, **la tentative s'affiche immédiatement dans le terminal**.  
❌ Si **aucune tentative échouée** n’a lieu, rien ne s'affiche.  

---

## 🔹 Fonctionnement du script Python (`analyse_logs.py`)  

📌 **Analyse approfondie des logs pour identifier les attaques.**  

- **Lecture complète** du fichier `/var/log/auth.log`.  
  - **Vérifie** que le fichier existe avant de l'ouvrir.  
  - **Lit** ligne par ligne les logs.  
- **Détection des tentatives d'intrusion** grâce à une **expression régulière (regex)** :  
  - **Capture l'adresse IP** de l'attaquant (**IPv4 ou IPv6**).  
  - **Capture l'utilisateur ciblé** (*valide ou `invalid user`*).  

**Exemple de ligne détectée** :  

```bash
Failed password for invalid user hacker from 192.168.1.5 port 50234 ssh2
```

## 📌 Comptabilisation des tentatives suspectes  
✔ Si une **IP a plusieurs échecs**, elle est considérée comme **suspecte**.  

---

## 📌 Génération d’un rapport de sécurité  
✔ **Liste les IP suspectes** et le **nombre de tentatives échouées**.  
✔ **Stocke les résultats** dans `rapports/analyse_logs_report.txt`.  

### 📜 **Exemple de rapport généré**  

```plaintext
📌 Rapport des tentatives de connexion échouées 📌
==================================================
🔴 192.168.1.5 - 3 tentatives échouées
🔴 10.0.0.1 - 5 tentatives échouées
```

## 🔹 Résultat attendu  
✅ **Un fichier rapport** est généré avec les **IP suspectes** et le **nombre de tentatives**.  
✅ **Si aucun échec de connexion** n’est détecté, **le rapport indique que tout est sécurisé**.  

---

## 📌 Explication des résultats observés lors des tests  

### 🖥️ **Exécution du script Bash (`monitor_auth_log.sh`)**  
✔ Si un utilisateur entre un **mauvais mot de passe** en SSH, **l’échec s'affiche instantanément**.  

🔎 **Vérification** : Faire un test en tentant de se connecter avec un **faux compte** :  
```bash
ssh faux_utilisateur@localhost
```

### 🖥️ Exécution du script Python (`analyse_logs.py`)  
✔ **Après plusieurs tentatives échouées**, le rapport **`analyse_logs_report.txt`** affiche les **IP suspectes**.  

🔎 **Vérification** : Vérifier que **l’IP du terminal utilisé** s’affiche bien en cas de tentatives d’accès infructueuses.  

### 🛡️ Protection contre les attaques par force brute avec Fail2Ban

Pour éviter les tentatives de connexion répétées par force brute sur SSH, nous avons configuré **Fail2Ban** afin de bloquer automatiquement les adresses IP après plusieurs échecs de connexion.

#### ✔ Configuration  
Nous avons activé **Fail2Ban** et défini une règle pour bannir une IP après **3 tentatives échouées**.

#### ✔ Résultat attendu  
- Lorsqu'un attaquant tente d'entrer plusieurs mauvais mots de passe, son IP est ajoutée à la liste des adresses bannies.  
- La commande suivante permet de voir les IP bannies :  
  ```bash
  sudo fail2ban-client status sshd
  ```
✔ Exemple d'IP bannie
bash
```
Banned IP list:
- 192.168.1.100
```

💡 Remarque
Si une IP a été bannie par erreur, elle peut être débloquée avec :

bash
```
sudo fail2ban-client set sshd unbanip <adresse_IP>
```

---

## 📌 Conclusion et pertinence par rapport à la cybersécurité  

### ✅ Détection des intrusions en temps réel  
✔ Permet d’**identifier rapidement une attaque en cours** (ex: brute force sur SSH).  
✔ **Réduit le risque d’accès non autorisé** en alertant immédiatement.  

### ✅ Analyse approfondie et traçabilité  
✔ Le script **Python offre un historique détaillé** des tentatives pour identifier les attaquants récurrents.  
✔ Utile pour **bloquer les IP suspectes** ou activer des contre-mesures comme **Fail2Ban**.  

➡️ **Grâce à ces deux scripts, nous mettons en place une surveillance efficace** pour renforcer la sécurité des connexions au serveur. 
