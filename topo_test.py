from mininet.topo import Topo
from mininet.link import Link,TCLink,Intf

class MyTopo( Topo ):
    "Simple topology example."

    def build( self,link=TCLink ):
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
        
        # add links
        # H1
        self.addLink(hosts[0],alss[0],cls=TCLink)
        self.addLink(hosts[0],alss[1],cls=TCLink)
        # H2
        self.addLink(hosts[1],alss[0])
        self.addLink(hosts[1],alss[1])
        # H3
        self.addLink(hosts[2],alss[0])
        self.addLink(hosts[2],alss[1])
        # H4
        self.addLink(hosts[3],alss[2])
        self.addLink(hosts[3],alss[3])
        # H5
        self.addLink(hosts[4],alss[2])
        self.addLink(hosts[4],alss[3])
        # H6
        self.addLink(hosts[5],alss[2])
        self.addLink(hosts[5],alss[3])
        # H7
        self.addLink(hosts[6],alss[4])
        self.addLink(hosts[6],alss[5])
        # H8
        self.addLink(hosts[7],alss[4])
        self.addLink(hosts[7],alss[5])
        # H9
        self.addLink(hosts[8],alss[4])
        self.addLink(hosts[8],alss[5])
        # H10
        self.addLink(hosts[9],alss[4])
        self.addLink(hosts[9],alss[5])

         # link ACL TO CORE level
        for i in range(0,6):
            self.addLink(alss[i],clss[0])
            self.addLink(alss[i],clss[1])
 

        
topos = { 'mytopo': ( lambda: MyTopo() ) }
