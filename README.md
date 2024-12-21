# RSX217_MINI-PROJ

## ENV preparation

Install tested on : UBUNTU 20.14

#### - update/upgrade host -
time : 20 mins
```
apt update
apt upgrade
```
#### - Install Mininet -

launch the script "script_install_mini.bash"

#### - Check mininet version install -
```
echo py sys.version | sudo mn -v output
```
-> python 3.8.10

#### - Check mininet install -

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
Dans un premier temps, il faut lancer le controller :
```
sudo /opt/onos-2.0.0/apache-karaf-4.2.2/bin/start
```
Dans un deuxieme temps, il faut lancer la CLI :
```
sudo /opt/onos-2.0.0/apache-karaf-4.2.2/bin/client
```
Une fois dans le controler, il faut activer le protocol openflow :
```
app activate org.onosproject.fwd
app activate org.onosproject.openflow
```
### 2. La topologie SND
Pour lancer la topologie, se rendre dans le dossier du GIT et lancier le script python :
```
sudo python3 topo_arch_sdn.py
```
### 3. Vérifier link state controller
Pour être sûr que la topologie s'est bien lancée, il faut vérifier l'état des liens entre les switchs et le controller :
```
sudo ovs-vsctl show
```
