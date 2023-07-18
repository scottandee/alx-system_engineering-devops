# 0x08 - NETWORKING BASICS #1
This project is the second in the series of networking projects. It's objective is to lear about computer networks

## Localhost
This is a computers loopback address. It has the entire 127.0.0.0/8 block reserved for this purpose. The default address is 127.0.0.1. This address can be used for various purposes including network troubleshooting, testing APIs, Security testing, site blocking, speed test.ifconfig interface_name up

### What is a Node
This is any device that is connected to a computer network

### What is a Host
This signifies any device or computer that has a unnique address ion a computer network

##  0.0.0.0
This address serves the purpose of indicating a "wildcard" or "unspecified" address. Some uses are to bind to all avaliable network interfaces, indicate default route, network configuration, address initialization, Network mask representation, socket binding etc.

## The `/etc/hosts` File
The purpose of this file is for address-name translation. When you type a web address into your browser, your browser will first look into the `/etc/hosts` file to confirm if that address is present in the file before it then consults the DNS. The file contains name and Ip addresses which are usually separated by tabs.

## The `nc` command

## The `ifconfig` command
This is short for interface configuration. It is used to view and configure network interfaces on the UNIX like OS. Some of the uses are
1. View Network Interfaces: this allows you to view all network interfaces ip, mac and status(up or down). This can be done by running the ifconfig command.
2. Activating and deactivating interfaces `ifconfig interface_name up` or `ifconfig interface_name up`
3. Setting IP addresses `ifconfig interface_name ip_address netmask subnet_mask`
4. Changing maximum transmission unit `ifconfig interface_name mtu new_mtu_value`
