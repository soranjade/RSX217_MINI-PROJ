from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch, Host
from mininet.link import TCLink
from mininet.cli import CLI

def topology():
    # Cr�er le r�seau
    net = Mininet(controller=Controller, switch=OVSSwitch, link=TCLink)

    # Ajouter le contr�leur
    c0 = net.addController('c0')

    # Ajouter les h�tes avec deux interfaces
    h1 = net.addHost('h1', ip=None)  # Pas d'IP par d�faut, car le bond aura l'IP
    h2 = net.addHost('h2')
    # Ajouter les switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    # Ajouter des liens entre h1 et les switches
    net.addLink(h1, s1, intfName1='h1-eth0')  # Premi�re interface
    net.addLink(h1, s2, intfName1='h1-eth1')  # Deuxi�me interface
    net.addLink(h2, s2)

    # Ajouter un lien entre les switches (si n�cessaire)
    net.addLink(s1, s2)

    # D�marrer le r�seau
    net.start()

    # Configurer l?agr�gation de liens sur l?h�te et les switches
    configure_lacp(h1, s1, s2)

    # Lancer l'interface CLI
    CLI(net)

    # Arr�ter le r�seau
    net.stop()

def configure_lacp(h1, s1, s2):
    # Configuration LACP sur l'h�te
    h1.cmd('modprobe bonding')
    h1.cmd('ip link add bond0 type bond')
    h1.cmd('ip link set dev bond0 type bond mode 802.3ad miimon 100')
    h1.cmd('ip link set h1-eth0 down')
    h1.cmd('ip link set h1-eth1 down')
    h1.cmd('ip link set h1-eth0 master bond0')
    h1.cmd('ip link set h1-eth1 master bond0')
    h1.cmd('ip link set bond0 up')
    h1.cmd('ip addr add 10.0.0.1/24 dev bond0')

    # Configuration LACP sur les switches (Open vSwitch)
    s1.cmd('ovs-vsctl add-bond s1 bond0 s1-eth1 s1-eth2 lacp=active')
    s2.cmd('ovs-vsctl add-bond s2 bond0 s2-eth1 s2-eth2 lacp=active')

if __name__ == '__main__':
    topology()
