"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""
#!/usr/bin/python

from mininet.node import Host,OVSSwitch,Controller
from mininet.link import Link

#add hosts & switches
h1=Host('h1')
h2=Host('h2')
h3=Host('h3')
h4=Host('h4')
s1=OVSSwitch('s1',inNamespace=False)
s2=OVSSwitch('s2',inNamespace=False)
c0=Controller('c0',inNamespace=False)

#add links
Link(h1,s1)
Link(h2,s1)
Link(h3,s2)
Link(h4,s2)
Link(s1,s2)

h1.setIP('10.0.0.1/24')
h2.setIP('10.0.0.2/24')
h3.setIP('10.0.0.3/24')
h4.setIP('10.0.0.4/24')

#controller
c0.start()

print h1.IP
print h2.IP
print h3.IP
print h4.IP

print 'Pinging...'
print 'kek'

s1.stop()
s2.stop()
c0.stop()
