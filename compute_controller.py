# 1 Recuper la topologie
# -- Recuperer tous les devices
# -- Recuperer tous les LINKS
# -- Creer le graph (NODE,LINKS) (dijsktra)
# 2 Compute des chemins
# -- Calculer les chemins plus courts (soit par dijsktra ou recuperer sur API ONOS directement)
# -- Calculer les chemins alternatifs
# 3 CRON toutes les 5s
# -- Recuperer le debit utilisé sur chaque lien
# -- Mettre un TRIGGER de seuil de debit
# -- SI TRIGGER -> Chemin ALTERNATIF
# -- SI Chemin ALTERNATIF, POST des FLOWS/Intents