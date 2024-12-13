from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."
        hosts = []
        alss = []
        clss = []
        # hosts creations 
        for i in range(1,11):
            hosts.append(self.addHost(f'H{i}'))
        # switch access level creations
        for i in range(1,7):
            alss.append(self.addSwitch(f'ALS{i}'))
        # switch core level creations
        for i in range(1,3):
            clss.append(self.addSwitch(f'CLS{i}'))

topos = { 'mytopo': ( lambda: MyTopo() ) }
