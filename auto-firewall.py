#!python
# Takes the output from nmap and automatically firewall all ports except 22/ssh
# To use, output nmap to a file and enter the file name as the only argument.

import sys
import subprocess

file = sys.argv[1]
protocol = sys.argv[2]

#if len(sys.argv)  < 2:
#  exit('Incorrect number of parameters')




if protocol is not 'tcp' or not 'udp':
  exit('incorrect protocol specified')

for line in open(file):
  if "open" in line:
    portnum = line.split("/")[0]
    new1 = portnum.replace("631","0" )
    var1 = ("echo", "iptables", "-I", "INPUT", "-p", new1, "--dport", protocol, "-j", "DROP" )# % (new1, protocol)
    subprocess.Popen(var1)
