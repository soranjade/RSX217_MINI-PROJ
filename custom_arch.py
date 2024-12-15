from mininet.topo import Topo
from mininet.node import Controller, OVSSwitch, Host
from mininet.link import TCLink
from mininet.cli import CLI

class MyTopo( Topo ):
    def build( self ):
        # Ajout du controleur
        #controller = self.addController('c0')
        
        hosts = []
        phosts = []
        ess = []
        css = []
        # hosts creations H1 -> H8
        for i in range(1,9):
            hosts.append(self.addHost(f'H{i}'))
        # hosts creations PH1 -> PH2
        for i in range(1,3):
            phosts.append(self.addHost(f'PH{i}'))
        # Edge switch creations ES1 -> ES4
        for i in range(1,5):
            ess.append(self.addSwitch(f'ES{i}',stp=True))
        # Core switch creations ES1 -> ES4
        for i in range(1,5):
            css.append(self.addSwitch(f'CS{i}',stp=True))
            
        # Link creation
        # ES1 -> H1/H2
        self.addLink(hosts[0], ess[0])
        self.addLink(hosts[1], ess[0])
        # ES2 -> H3/H4
        self.addLink(hosts[2], ess[1])
        self.addLink(hosts[3], ess[1])
        # ES3 -> H5/H6
        self.addLink(hosts[4], ess[2])
        self.addLink(hosts[5], ess[2])
        # ES4 -> H7/H8
        self.addLink(hosts[6], ess[3])
        self.addLink(hosts[7], ess[3])
        # CS4 -> PH9
        self.addLink(phosts[0], css[3])
        # CS2 -> PH10
        self.addLink(phosts[1], css[1])
        # - CS BACKBONE -
        self.addLink(css[0], css[1])
        self.addLink(css[1], css[2])
        self.addLink(css[2], css[3])
        self.addLink(css[3], css[0])
        # - CS -> ES -
        # ES1 -> CS1/CS4
        self.addLink(css[0], ess[0])
        self.addLink(css[3], ess[0])
        # ES2 -> CS1/CS2
        self.addLink(css[0], ess[1])
        self.addLink(css[1], ess[1])
        # ES3 -> CS2/CS3
        self.addLink(css[1], ess[2])
        self.addLink(css[2], ess[2])
        # ES4 -> CS3/CS4
        self.addLink(css[2], ess[3])
        self.addLink(css[3], ess[3])
    
topos = { 'mytopo': ( lambda: MyTopo() ) }