"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class myfirsttopo(Topo):
    "Simple topology example."

    def __init__(self):
        "Create custom topo."
        Topo.__init__(self)

        #add hosts & switches
        h1=self.addHost('h1')
        h2=self.addHost('h2')
        h3=self.addHost('h3')
        h4=self.addHost('h4')
        h5=self.addHost('h5')
        h6=self.addHost('h6')
        h7=self.addHost('h7')
        h8=self.addHost('h8')
        s1=self.addSwitch('s1')
        s2=self.addSwitch('s2')
        s3=self.addSwitch('s3')
        s4=self.addSwitch('s4')
        s5=self.addSwitch('s5')
        s6=self.addSwitch('s6')
        s7=self.addSwitch('s7')

        #add links
        self.addLink(h1,s1)
        self.addLink(h2,s1)
        self.addLink(h3,s2)
        self.addLink(h4,s2)              
        self.addLink(h5,s3)
        self.addLink(h6,s3)
        self.addLink(h7,s4)
        self.addLink(h8,s4)
        self.addLink(s1,s5)
        self.addLink(s2,s5)
        self.addLink(s3,s6)
        self.addLink(s4,s6)
        self.addLink(s5,s7)
        self.addLink(s6,s7)

def runExperiment():
    print "simple mininet experiment"
    topo=myfirsttopo()
    net=Mininet(topo)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "testing network connectivity"
    net.pingAll()
    net.stop()

if __name__ =='__main__':
    setLogLevel('info')
    runExperiment()
