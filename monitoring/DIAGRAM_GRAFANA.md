# Install et config Diagram for Grafana

## install plugin Diagram

- Aller dans le menu -> Administration -> Plugins and data -> Plugins
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
- On va modifier le nom des metrics dans la légende:
   - Dans le cadre query, en bas, on va à la dernière ligne "Options" et dans le champs "legends" on choisit custom et on met : {{node}}_{{port}}_recv
   - On valide avec le bouton bleu à droite "Run queries"
- On va ajouter les metrics "sent":
  -   On va sur la query C modifiée précédemment
  -   On clique sur l'icone "duplicate query" (2ième icone dans le coin à droite au bout de la ligne C)
  -   Dans la ligne "Metrics Browser" on met : irate(onos_device_bytes_sent{}[15m]) à la place de irate(onos_device_bytes_received{}[15m])
  -   Comme précédemment on modifie le nom de la metrics dans la légende, on mets: {{node}}_{{port}}_sent
    
- On va maintenant créer le schéma de la topo et  modifier plusieurs options: On va dans le cadre qui est dans la partie droite de  la page
  - On modifie le titre: Bytes received/sent per Port per second
  - Dans le bloc "Diagram definition " on met le contenu du fichier  [diag_def.txt](diag_def.txt)  
  -  Minimum text node width : 50
  -  Minimum text node height : 30
  -  Legend : on décoche
  -  Advanced: on clique sur " + Add Metric Character Remplacement "
     -  String or Regex to match against metric name :  of_00000000000000
     -  Replacement expression/text : vide
  - Thresold : rouge -> 8000
- On sauve le dashbord (bouton bleu "Save dashbord" en haut à droite) et clique sur "back to dashbord"
- Si besoin on refresh la page pour que le new dashbord soir pris en compte
- Sur la page principale du dashbord on ajuste le panneau modifié à une taille "maximale"
- Enfin on met le "refresh" à 5s en haut à droite

**Rq:** Il semble y avoir un bug d'affichage avec le plugin diagram: les panneaux ne se rafraichissement pas bien par moment et affichent un peu n'importe quoi.  
Pour pallier à cela, laisser un panneau "bidon" en premier 

