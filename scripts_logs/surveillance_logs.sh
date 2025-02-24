#!/bin/bash

# Surveiller auth.log en temps réel pour détecter les échecs de connexion
LOG_FILE="/var/log/auth.log"

echo "🔍 Surveillance en temps réel des échecs de connexion dans $LOG_FILE"
tail -f $LOG_FILE | grep --line-buffered "Failed password" | awk '{print "⚠️ Tentative de connexion échouée : " $0}'
