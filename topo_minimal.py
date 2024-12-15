from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink

def simpleTopology():
    net = Mininet(controller=Controller, link=TCLink)
    
    controller = net.addController('c0')
    
    h1 = net.addHost('H1', ip='10.0.0.1/24', defaultRoute='via 10.0.0.254')
    h2 = net.addHost('H2', ip='10.0.0.2/24', defaultRoute='via 10.0.0.254')
    
    s1 = net.addSwitch('S1')
    
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    
    net.start()
    
    CLI(net)
    net.stop()

if __name__ == '__main__':
    simpleTopology()
