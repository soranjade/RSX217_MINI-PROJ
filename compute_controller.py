# 1 Recuper la topologie
# -- Recuperer tous les devices 15 mins (test existant)
# -- Recuperer tous les LINKS 15 mins (test existant)

# 2 Compute des chemins 4/5h
# -- Creer le graph (NODE,LINKS) (dijsktra)
# -- Calculer les chemins plus courts (soit par dijsktra ou recuperer sur API ONOS directement)
# -- Calculer les chemins alternatifs

# 3 CRON toutes les 5s
# -- Recuperer le debit utilisé sur chaque lien
# -- Mettre un TRIGGER de seuil de debit
# -- SI TRIGGER -> Chemin ALTERNATIF
# -- SI Chemin ALTERNATIF, POST des FLOWS/Intents 3h