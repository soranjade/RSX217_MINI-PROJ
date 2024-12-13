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
            
        hosts[0].cmd('modprobe bonding')
        hosts[0].cmd('ip link add bond0 type bond')
        hosts[0].cmd('ip link set dev bond0 type bond mode 802.3ad miimon 100')
        hosts[0].cmd('ip link set H1-eth0 down')
        hosts[0].cmd('ip link set H1-eth1 down')
        hosts[0].cmd('ip link set H1-eth0 master bond0')
        hosts[0].cmd('ip link set H1-eth1 master bond0')
        hosts[0].cmd('ip link set bond0 up')
        hosts[0].cmd('ip addr add 10.0.0.1/24 dev bond0')
        
        #alss[0].cmd('ovs-vsctl add-bond ALS1 bond0 ALS1-eth1 ALS2-eth1 lacp=active')
        #alss[1].cmd('ovs-vsctl add-bond ALS2 bond0 ALS2-eth1 ALS1-eth1 lacp=active')
        
topos = { 'mytopo': ( lambda: MyTopo() ) }
