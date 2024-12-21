# RSX217_MINI-PROJ

## ENV preparation

Install tested on : UBUNTU 20.14

### - update/upgrade host -
time : 20 mins
```
apt update
apt upgrade
```
### - Install Mininet -

launch the script "script_install_mini.bash"

### - Check mininet version install -
```
echo py sys.version | sudo mn -v output
```
-> python 3.8.10

### - Check mininet install -

```
sudo mn
```
```
pingall
exit
```
```
sudo mn -c
```
#### Installation ONOS
```
apt update
apt install -y docker-compose
docker pull onosproject/onos:2.7-latest
```


   
## Lancement de la topologie

### 1. Le controller
Lancer le compose dans le dossier "compose"
```
docker compose up
```
Se rendre dans le container
```
docker exec -it onos_270-onos-1 bash
```

Lancer le "client" :
```
./apache-karaf-4.2.14/bin/client
```

Une fois dans le controler, il faut activer le protocol openflow et la reactive forwarding :
```
app activate org.onosproject.fwd
app activate org.onosproject.openflow
```
### 2. La topologie SND
Pour lancer la topologie, se rendre dans le dossier du topo et lancier le script python :
```
sudo python3 topo_stable.py
```
### 3. Vérifier link state controller
Pour être sûr que la topologie s'est bien lancée, il faut vérifier l'état des liens entre les switchs et le controller :
```
sudo ovs-vsctl show
```
