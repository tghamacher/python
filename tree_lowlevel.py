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
h5=Host('h5')
h6=Host('h6')
h7=Host('h7')
h8=Host('h8')


s1=OVSSwitch('s1',inNamespace=False)
s2=OVSSwitch('s2',inNamespace=False)
s3=OVSSwitch('s3',inNamespace=False)
s4=OVSSwitch('s4',inNamespace=False)
s5=OVSSwitch('s5',inNamespace=False)
s6=OVSSwitch('s6',inNamespace=False)
s7=OVSSwitch('s7',inNamespace=False)
c0=Controller('c0',inNamespace=False)

#add links
Link(h1,s1)
Link(h2,s1)
Link(h3,s2)
Link(h4,s2)
Link(h5,s3)
Link(h6,s3)
Link(h7,s4)
Link(h8,s4)
Link(s1,s5)
Link(s2,s5)
Link(s3,s6)
Link(s4,s6)
Link(s5,s7)
Link(s6,s7)


h1.setIP('10.0.0.1')
h8.setIP('10.0.0.8')

c0.start()
s1.start([c0])
s2.start([c0])
s3.start([c0])
s4.start([c0])
s5.start([c0])
s6.start([c0])
s7.start([c0])

print h1.IP
print h2.IP
print h3.IP
print h4.IP
print h5.IP
print h6.IP
print h7.IP
print h8.IP

print 'Pinging...'
print h1.cmd( 'ping -c4 ', h8.IP() )


s1.stop()
s2.stop()
s3.stop()
s4.stop()
s5.stop()
s6.stop()
s7.stop()
c0.stop()
