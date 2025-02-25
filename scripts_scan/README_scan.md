# 🔍 Scan des Ports et Services Ouverts  

## 📌 Objectif global  
L’objectif de cette partie est de détecter les ports ouverts et les services actifs sur une cible (adresse IP ou site web) à l’aide de **nmap**.  

Deux scripts sont utilisés :  
✔ **Script Bash** (`scan_ports.sh`) pour un scan simple et rapide.  
✔ **Script Python** (`scan_ports.py`) pour une meilleure gestion des erreurs et une flexibilité accrue.  

---

## Fonctionnement du script Bash (`scan_ports.sh`)  

### Description  
- Effectue un scan des ports ouverts avec **nmap** et affiche les résultats.  
- Vérifie si une adresse IP est fournie en argument, sinon affiche un message d’erreur.  
- Génère un fichier de rapport horodaté sous la forme :  
  ```bash
  rapports/Bash_scan_result_192_168_1_1_20250224_153000.txt 
  
- Utilise les options suivantes de **nmap** :  
 `-Pn` : Ignore le ping et scanne directement les ports.  
 `-sV` : Identifie les services derrière les ports ouverts.  
- Enregistre les résultats dans un fichier et les affiche dans le terminal.  

### ✅ Résultats attendus  
✔ **Ports ouverts affichés** avec leur service associé.  
✔ **Rapport généré** dans le dossier `rapports/`.  
❌ **Échec** si `nmap` n'est pas installé.  

---

## Fonctionnement du script Python (`scan_ports.py`)  

### Description  
- Effectue le **même scan** que le script Bash, mais avec **plus de contrôle**.  
- Vérifie si une adresse IP ou un nom de domaine est fourni, sinon affiche une erreur.  
- Génère un fichier de rapport horodaté, comme dans le script Bash.  
- Exécute `nmap` via Python (`subprocess.run`), en utilisant :  
- `-Pn` : Ignore le ping.  
- `-sV` : Identifie les services actifs.  
- Capture et affiche les résultats **en temps réel**.  
- Enregistre les résultats dans `rapports/` sous un **nom unique**.  
- Gère les erreurs possibles :  
- Vérifie si `nmap` est installé et affiche un message d'erreur si ce n'est pas le cas.  
- Capture et affiche les erreurs de subprocess.  

### Résultats attendus  
✔ **Même sortie** que le script Bash (détection des ports ouverts).  
✔ **Meilleure gestion des erreurs** (installation de `nmap`, erreurs `subprocess`).  
✔ **Facilement intégrable** dans d'autres outils Python.  

---

## Comparaison entre les deux scripts  

| Critère                  | Script Bash (`scan_ports.sh`) | Script Python (`scan_ports.py`) |
|--------------------------|-----------------------------|--------------------------------|
| **Langage**              | Bash (shell script)         | Python (`subprocess`)         |
| **Facilité d’exécution** | Simple, rapide             | Plus structuré et flexible    |
| **Gestion des erreurs**  | Basique (pas de vérification de `nmap`) | Vérifie si `nmap` est installé et capture les erreurs |
| **Flexibilité**          | Exécutable directement en terminal | Intégrable dans des outils Python |
| **Affichage des résultats** | Affiche après le scan | Affiche en temps réel |
| **Stockage des rapports** | ✔ Oui (`rapports/`) | ✔ Oui (`rapports/`) |

➡️ **Le script Bash** est idéal pour un scan rapide en ligne de commande.  
➡️ **Le script Python** est plus robuste et permet une meilleure intégration dans des outils avancés.  

## Explication des résultats observés lors des tests  

### ▶️ Exécution du script Bash (`scan_ports.sh`)  
✔ **Exécution rapide** avec un fichier de rapport généré.  
✔ **Affichage des ports ouverts et des services détectés**.  
✔ **Vérification** que le rapport est bien stocké dans `rapports/`.  

### ▶️ Exécution du script Python (`scan_ports.py`)  
✔ **Résultats identiques** à ceux du script Bash.  
✔ **Affichage en direct** des résultats dans le terminal.  
✔ **Gestion des erreurs améliorée** (ex : si `nmap` n’est pas installé).  

---

## Conclusion et pertinence en cybersécurité  

### Détection des services en écoute sur un serveur  
✔ Permet d’**identifier les ports ouverts et les services actifs**.  
✔ Utile pour **anticiper les vulnérabilités et sécuriser un réseau**.  

### Complémentarité entre Bash et Python  
✔ **Bash** est idéal pour un usage simple et rapide.  
✔ **Python** offre plus de contrôle et de flexibilité pour une intégration avancée.  

➡️ **Grâce à ces deux scripts, nous avons une solution efficace pour analyser un réseau et détecter d’éventuelles failles de sécurité.** 

