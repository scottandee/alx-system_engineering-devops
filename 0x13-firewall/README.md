# 0x13 - Firewall
A firewall is a tool that is used to filter out incoming and outgoing traffic depending on the type of configurations that it is given. In this project, we lern how to configure firewalls on our server, block out incoming traffic on specific ports and implement port forwarding.

## Types of Firewall
[Firewalls] (https://en.wikipedia.org/wiki/Firewall_%28computing%29) are classified based on Network-based or Host-based system.
* **Network-based Firewalls**: They are used to control the flow of data between networks and usually put in between WANs and LANs(which are private networks).
* **Host-based Firewalls**: These are usually installed on the host itself to control network traffic

### Note
* Host is identified by an ip address while port specifies a particular service which has a unique port number. 
* `port + ip = socket`

## Here are useful resources:
* [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-20-04)
* [Bob Cares](https://bobcares.com/blog/ufw-port-forwarding/)
