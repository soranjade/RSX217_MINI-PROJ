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

## Lancement de la topologie

### 1 Le controller
Dans un premier temps, il faut lancer le controller :
```
sudo ./opt/onos-2.0.0/apache-karaf-4.2.2/bin/start
```
Dans un deuxieme temps, il faut lancer la CLI :
```
sudo ./opt/onos-2.0.0/apache-karaf-4.2.2/bin/client
```
Une fois dans le controler, il faut activer le protocol openflow :
```
app activate org.onosproject.fwd
app activate org.onosproject.openflow
```

Pour lancer la topologie :
```
sudo python3 topo_arch_sdn.py
```
