# 0x09 - WEB INFRASTRUCTURE DESIGN
The objective of this project is to understand and whiteboard a simple webstack that uses a LAMP stack. To acheive this, we have to understand DNS and how it works, servers, server monitoring, load-balancing, firewall and web server.

## DNS
This stands for the Domain Name System. ICANN(International Corporation for Assigned Names and Numbers), a non-profit organization is responsible for control and coordination of the DNS. The role of the DNS is to translate A records into IP addresses. When you type in an address into your browser, it goes through a ton of work before your request gets to the server. Computers operate at high speeds so we do not notice this. The processes involved are:
* First, the browser cache will be checked and then the OS cache will be checked for the A record that you entered. If not found, it'll go to the next stop
* Next, the Resolver will be contacted. This resolver is usually your ISP. All resolvers know where to find the root server
* The root server always knows where to find the TLD server. There are 13 root name servers that exist today. They sit at the top of the DNS heirarchy. Each of these root servers are managed by 12 independent organizations around the world. These organizations provide servers that are scattered all around the world
* The TLD will search its cache, If it doesn't find it, It'll give you the address of the name servers.
    Types of TLDs
    * Country Code: `.uk`,`.fr`, `.ng`
    * Generic TLDs: `.net`, `.org`
    * Infrastructure TLDs: `.arpa` 
* The name servers can resolve any managed by the A record you passed

### Types of Domain Name Records
1. **A Records**: This translates into an IP address
2. **Canonical Name Record**: This translates into another domain name
3. **Mail Exchanger Record**: Specifies the name server responsible for accepting email messages on behalf of the domain
4. **TXT**: Ability to associatr arbitrary text with hostname

## Software Monitoring
This is used to watch computer metrics, record them and emit an alert if something unusual has happened. There are two phases to this.
1. Application Monitoring: this is about getting data about your running software and making sure it is running as expected
2. Server Monitoring: This is about getting information about your server and making sure it is not overloaded

## Web Server
The Web Server is a combination of hardware and software that delivers webpages. Hardware in the sense that storage is needed for the webserver files i.e codebase and Software which is the software that controls how http requests are received and responded to. It accepts requests via HTTP/HTTPS. Once an HTTP request it made for the ip address of a particular server the server reaches for the static content to then send back as response. In the case that there is dymanic content requested, the server sends a serverlet to the application server

## Application Server
This is used to serve dynamic content. This communicates with the database to reteive specific information. In essence, It provides business logic to the site. Business logic is the programming that manages communication between the end user and the database.

## What is a Server?
A server is any hardware or software machine that provides services/functionality to the clients.

## What is a SPOF
This stands for single point of failure. This is a point on your webstack in which when destroyed will cause the whole web infrastructure to go down as there is no replacement provided in the design. This causes downtime/unavaliability of a particular domain.

## Firewall
A firewall is used to monitor all **incoming** and **outgoing** traffic. The firewall has to be configured in order to specify what you dont want to pass through. It can be hardware(In between the gateway and your network) or software(Installed on your server).

## SSL
An ssl certificate enables encryption of communication in between your server and a client

**Note**
* Scale up: Increase server specifications
* Scale out: Adding more Servers

## AUTHOR
* Olayinkascott Andee(andeeolayinkascott@gmail.com)
