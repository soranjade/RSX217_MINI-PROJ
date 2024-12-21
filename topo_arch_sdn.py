from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch, Host, RemoteController
from mininet.link import TCLink
from mininet.cli import CLI

def topology():
    net = Mininet(controller=RemoteController,switch=OVSSwitch)
    # Ajout du controleur
    c0 = net.addController('c0', controller=RemoteController)
    
    hosts = []
    phosts = []
    ess = []
    css = []
    # hosts creations H1 -> H8
    for i in range(1,9):
        hosts.append(net.addHost(f'H{i}'))
    # hosts creations PH1 -> PH2
    for i in range(1,3):
        phosts.append(net.addHost(f'PH{i}'))
    # Edge switch creations ES1 -> ES4
    for i in range(1,5):
        ess.append(net.addSwitch(f'ES{i}',dpid=f'00000000010{i}', protocols='OpenFlow13'))
    # Core switch creations CS1 -> CS4
    for i in range(1,5):
        css.append(net.addSwitch(f'CS{i}',mac=f'00000000020{i}', protocols='OpenFlow13'))
        
    # Link creation
    # ES1 -> H1/H2
    net.addLink(hosts[0], ess[0])
    net.addLink(hosts[1], ess[0])
    # ES2 -> H3/H4
    net.addLink(hosts[2], ess[1])
    net.addLink(hosts[3], ess[1])
    # ES3 -> H5/H6
    net.addLink(hosts[4], ess[2])
    net.addLink(hosts[5], ess[2])
    # ES4 -> H7/H8
    net.addLink(hosts[6], ess[3])
    net.addLink(hosts[7], ess[3])
    # CS4 -> PH9
    net.addLink(phosts[0], css[3])
    # CS2 -> PH10
    net.addLink(phosts[1], css[1])
    # - CS BACKBONE -
    net.addLink(css[0], css[1])
    net.addLink(css[1], css[2])
    net.addLink(css[2], css[3])
    net.addLink(css[3], css[0])
    # - CS -> ES -
    # ES1 -> CS1/CS4
    net.addLink(css[0], ess[0])
    net.addLink(css[3], ess[0])
    # ES2 -> CS1/CS2
    net.addLink(css[0], ess[1])
    net.addLink(css[1], ess[1])
    # ES3 -> CS2/CS3
    net.addLink(css[1], ess[2])
    net.addLink(css[2], ess[2])
    # ES4 -> CS3/CS4
    net.addLink(css[2], ess[3])
    net.addLink(css[3], ess[3])
    net.start()
    # Lancer l'interface CLI
    CLI(net)
    
if __name__ == '__main__':
    topology()
        
