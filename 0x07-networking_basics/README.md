# 0x07 - NETWORKING BASICS

## The OSI MODEL: The Open Systems Interconnection Model
This is a conceptual textbook model that describes how computer systems and all other devices communicate over a computer network. "Please Do Not Throw Susage Pizza Away"

1. Physical Layer: responsible for transmitting raw bits of data across a physical connection. Establish, terminate and maintain physical connection between devices. Examples are hubs, NICs(Network Interface Cards), modems, cables and connectors. The functions of this layer are:
    * Physical media specification: types of wires used, 
    * Physical topology: Bus, star, 
    * Physical addressing: mac addressing
    * Transmission rate and bandwidth
    * Data encoding and signaling
2. Data Link Layer: This translates the raw bits of data into frames, it ensures that this raw bits of data are transmitted to the right destination. In essence, it plays a crucial role inestablishing a reliable and error free link between two devices that are connected on the same local network segment. The ethernet lives on this layer. The functions of this layer are:
    * Frame delimitation: breaking down data into frames
    * Addressing and identification
    * Media Access Control
    * Error Detection and Handling
  
    It is subdivided into Media Access Control and Logical Link Control layer
3. Network Layer: Responsible for routing data frames across different networks. The Ip part of TCP/IP is a good example.
4. Transport Layer: This layer manages end to end connection between two nodes. Examples are TCP(Transmission control protocol) and UDP(User datagraam protocol).
5. Sesssion Layer: This manages the sessions between two devices over a network. It takes cere of authentication and reconnection. An example is SQL
6. Presentation Layer:  It focuses on the formatting, conversion, and encryption of data to ensure that information exchanged between different systems can be understood and interpreted correctly
7. Application Layer: This is the interface between the user and the network. An example is HTTP
