# Install et config Diagram for Grafana

## install plugin Diagram

- Aller dans le mnnu -> Administration -> Plugins and data -> Plugins
- Chercher diagram dans la barre de recherche puis cliquer dessus en bouton  bleu "installer" en haut à droite

## Modif du dashbord SND_EXPORTER

On va modifier le dashbord SND_EXPORTER en replaçant les types de graph par Diagram

- Aller dans le dashbord Onos Dashborg (installé avec le sdn_exporter)
- Supprimer tous les panneux sauf
  - Bytes received per Port per second
  - Bytes sent per Port per second
( dans chaque panneau on clique dans le coin en haut à droite, les 3 points, puis "Remove")
- On édite dans le panneau Bytes received per Port per second (on clique dans le coin en haut à droite, les 3 points, puis "Edit")
- En haut à droite on change le type de graph: par défaut c'est Time Serie et on met Diagram
- On va tunner ce plugin en modifiant les options: (partie droite de  la page)
  - Dans le bloc "Diagram definition " on met le contenu du fichier  [diag_def.txt](diag_def.txt)  
  -  Minimum text node width : 80
  -  Minimum text node height : 80
  -  Legend : on décoche
  -  Advanced: on clique sur " + Add Metric Character Remplacement "
     -  String or Regex to match against metric name :  _instance__172.17.0.1_9091__ job__prometheus__ node__of_00000000000000
     -  Replacement expression/text : vide
  - Thresold : rouge -> 8000
- On sauve le dashbord (bouton bleu "Save dashbord" en haut à droite) et clique sur "back to dashbord"
- Si besoin on refresh la page pour que le new dashbord soir pris en compte
- On fait tout pareil pour le panneau "Bytes received per Port per second"
- Sur la page principale du dashbord on ajouter les 2 panneaux 

