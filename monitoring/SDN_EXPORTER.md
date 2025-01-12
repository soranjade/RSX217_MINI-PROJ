# Install SDN_EXPORTER

## Recup du projet
```
mkdir ~/sdnprom
git clone https://github.com/querciak/SDN-prometheus.git
cd SDN-prometheus
 
pip install -r requirement.txt
 
# on lance l'exporter
python3 exporter.py
```
## Intégration dans prometheus

```
# On ajoute à la fin dans le section targets du fichier /opt/monitoring/etc/prometheus/prometheus.yml 
          - 1172.17.0.1:9091

# on reload prometheus
curl -X POST http://localhost:9090/-/reload

```
RQ: l'ip c'est celle du pont docker

## Intégration dans grafana
- On va dans l'interface web de grafana
- On va dans le menu (en haut à gauche) -> Dashboard -> bouton à droite "New" -> import 
- Dans le cadre upload on met le fichier project21_dashboard.json du projet GitHub puis "import"

