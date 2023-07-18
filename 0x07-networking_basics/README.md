# 0x07 - NETWORKING BASICS

## The OSI MODEL: The Open Systems Interconnection Model
This is a conceptual textbook model that describes how computer systems and all other devices communicate over a computer network. "Please Do Not Throw Susage Pizza Away"

1. **Physical Layer**: responsible for transmitting raw bits of data across a physical connection. Establish, terminate and maintain physical connection between devices. Examples are hubs, NICs(Network Interface Cards), modems, cables and connectors. The functions of this layer are:
    * Physical media specification: types of wires used, 
    * Physical topology: Bus, star, 
    * Physical addressing: mac addressing
    * Transmission rate and bandwidth
    * Data encoding and signaling
2. **Data Link Layer**: This translates the raw bits of data into frames, it ensures that this raw bits of data are transmitted to the right destination. In essence, it plays a crucial role inestablishing a reliable and error free link between two devices that are connected on the same local network segment. The ethernet lives on this layer. The functions of this layer are:
    * Frame delimitation: breaking down data into frames
    * Addressing and identification
    * Media Access Control
    * Error Detection and Handling
  
    It is subdivided into Media Access Control and Logical Link Control layer
3. **Network Layer**: Responsible for routing data frames across different networks. The Ip part of TCP/IP is a good example.
4. **Transport Layer**: This layer manages end to end connection between two nodes. Examples are TCP(Transmission control protocol) and UDP(User datagraam protocol).
5. **Sesssion Layer**: This manages the sessions between two devices over a network. It takes cere of authentication and reconnection. An example is SQL
6. **Presentation Layer**:  It focuses on the formatting, conversion, and encryption of data to ensure that information exchanged between different systems can be understood and interpreted correctly
7. **Application Layer**: This is the interface between the user and the network. An example is HTTP

## WAN
This is a network that spans over a long range. It can be referred to as an interconnection of wants. A typical example is the internet.

## LAN
this stands for Local area network
This covers and interconnects  a short range. example are an office building, your home etc

## MAC
it is a string of characters that Identifies a device on a network. When a new device is created, it is assigned a Mac address which is attached the a key computer device called the Network interface card. The MAC address is hard wired into the computers NIC. ARP translates your IP address into MAC address

## IP address 
this is a unique identifier of a computer on the internet. It can be IPV4 or IPV6. There can also be Private and Public Addresses
* Public Addresses: This is the unique address assigned to each user on the internet
* Private Addresses: this is the address assigned by the owner or manager to each device on a private network. This allows organizations to create their own computer networks.

## Localhost
This address refers to the current machine that you are using

## TCP and UDP
TCP is a transport layer protocol that that breaks town data into tcp segments for transportation. This protocol has an inbuilt error checking model eith which it ensures that data sent from the sender reaches the receiver. The UDP protocol splits data into UDP datagrams and sends to the receiver. There is no inbuilt error checking in this and for this reason, it is faster that the TCP model.

## What is a Host 
A host is any device that is connected to a network and has a unique IP address

## `ping` Command
This command is used to test network connectivity between two devices.
* The -c flag can be used to specify the number of times that you want to ping the host
* The ping command can accept A records and Ip addresses. Passing A records to the ping commands allows for testing name addresss resolution.
* You can also use this command to test your network interface card by running the ping command with your localhost address
If everything works fine, then we confirm that we are connected to the internet. It also confirms that all of your hardware are working correctly. This indicates thet the issue you're facing is related to software and not hardware. So it's most likely related to the browser or a firewall issue

## `netstat` Command
This stands for Network Statistics. It can be used to diagnose software issues and monitor network connections. Some flags are:
* `-t` for tcp
* `-u` for udp
* `-l` for listening ports
* `-n` for numerical ports instean of names

Some common TCP states are:
1. Listen: The server is listening for incoming connections
2. Established: The connection is open and data is being exchanged
3. Time_wait: the connection is waiting to terminate gracefully
4. Close_wait: the connection is close on the remote end but is waiting to be closed on the local end

## Author
* Olayinkascott Andee(andeeolayinkascott@gmail.com)



  
