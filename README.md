# Dynamic Host Blocking System (SDN Project)

## Problem Statement
Implement a system to dynamically block hosts using SDN based on MAC address.

## Tools Used
- Mininet
- POX Controller
- Ubuntu

## Steps
1. Run controller:
   python3 pox.py openflow.of_01 --port=6633 forwarding.firewall

2. Run Mininet:
   sudo mn --controller=remote,ip=127.0.0.1,port=6633 --topo single,3

3. Check MAC:
   h2 ifconfig

4. Update MAC in firewall.py

5. Test:
   h1 ping h2 (blocked)
   h1 ping h3 (allowed)

## Output
- Blocking successful for selected host
- Normal communication for others
