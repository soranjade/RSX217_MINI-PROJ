# Install Prometheus/Grafana 

## docker 

```
docker pull grafana/grafana
docker pull prom/prometheus

```
##  Conf

```
cd monitoring
sudo ./install.sh

```

   
## Lancement

```
docker-compose -f compose.yml  up
```

RQ: attendre un peu la première fois car la création du la bdd pour grafana prends quelques instants (30s)


## Connection 

### prometheus

http://127.0.0.1:9090


### Rq1
Si on va dans le menu "Status" -> "Targer Health" on peut voir la/les machines monitorées

### Rq2
Pour faire une modif sur prometheus on modifie le fichier /opt/monitoring/etc/prometheus/prometheus.yml.  
Et pour qu'il soit prit en compte on lance

```
curl -X POST http://localhost:9090/-/reload
```



### grafana 

http://127.0.0.1:3000

login/passwd par défaut: admin/admin  
Grafana demande de le changer la première fois


## Coupler grafana avec prometheus

On va dans l'interface web de grafana puis:

- on va dans le menu en haut à gauche (les 3 traits horizontaux)
- on choisit "connection"
- on cherche prometheus dans la barre de recherche et on clique dessus
- on clique sur "add new data source"
- dans la partie "Connection" on met l'url http://prometheus:9090
- enfin on va en bas et on clique sur le bouton  "Save and test"



## Arrêt des container prometheus/grafana
Dans le terminal où on a lancé le "docker-compose" on fait CTRL+c  puis 
```
docker-compose -f compose.yml down 

```

## Installation de SDN_EXPORTER
[Voir le fichier SDN_EXPORTER.md](SDN_EXPORTER.md)

## Install et confid du dashbord diagram
[Voir le fichier DIAGRAM_GRAFANA.md](DIAGRAM_GRAFANA.md)



