# 0x0C - WEB SERVER
In this project, we are tasked to set up the nginx web-server on our server

## What is a Web Server?
The main purpose of a web server is to serve up static content to clients. When serving static content if there is need for business logic in the site, then a serverlet will be sent to the application server and then the database will be contacted for information.

## About Nginx
Nginx is a webserver that can alsobe used as a reverse proxy, load balancer, and also a HTTP cache. The software was created by Igor Sysoev and released in 2004. With Nginx, setting up a server to serve static content is made easy.

## A Brief Review about How the Web Works
There are two major parties that we have to recognize on the web, the server and the client. The client is basically anyone that wants to access some content online. The server has the duty of providing functionality/web-services to the client i.e sending webpages back to the client. The other parts involved in this 
are:
1. Your Internet Connection: This basically allows us to access content on the web
2. TCP/IP: This serves as the means for transmitting our requests and responses all around the web
3. DNS: This is like an address book that translates A records into IP addresses
4. HTTP: This is the protocol that is used for communication between you browser and the server

## Demistifying Nginx Web Server Configuration
### What are Server Blocks?
Server blocks in nginx are like Virtual Hosts in apache2. It can be used to encapsulate configuration details and host more than one domain on a single server. It can also be referred to as a configuration block that defines how a webserver shoould handle requests for a specific domain or virtual host. The default server block file is `/etc/nginx/sites-available/default`. This file will suffice if you're only using one domain. In the case that there will be different domains, do create a file for each domain e.g `/etc/nginx/sites-available/example.com` and `/etc/nginx/sites-available/test.com`

This is the server block configuration for the default server
```bash
server {
   (1) listen 80 default_server;
        listen [::]:80 default_server;

   (2)  root /var/www/html;
        index index.html index.htm index.nginx-debian.html;

   (3)  server_name _;

   (4)   location / {
                try_files $uri $uri/ =404;
        }
}
```
1. This is the listen directive that tells the webserver what port to listen on
2. This is the directory from which the webserver will serve documents from.
3 This `_` is a placeholder for the domain name we want to serve. You can add aliases.
4. The location section is used to define how the web server should handle requests from specific URLs or URIs. `location /` defines how the web server should handle queries from the root, `location /images/` runs when we query like `www.test.com/images/`. There is no limit to the amount of location blocks that can be specified.
 
**Note**: Only one of our server block configs can have the default_server option enabled on the listen directive

Refer to [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04) for more information on this.

## What is Root Domain Name, Subdomain?
A Root Domain is a particular A record that translates to a particutar IP address. A domain name consists of a second level domain, a dot and a top level domain.
The Subdomain usually comes before the main domain. It can be used to create separate sections of a website, point to specific server or services or organizing resources in a more structured manner. For example, `blog.test.com` for the blog, `www.test.com` for the webserver itself, `mail.test.com` for the websites mail. Subdomains are usually set up by configuring the DNS records of your domain name.

![image](https://github.com/scottandee/alx-system_engineering-devops/assets/85585168/d34c88be-374f-478d-9e8b-1a1d911d8578)

The top level domain is the `.com` at the end of the main domain

## HTTP Requests
1. GET: This is used to ask for the html,css content of a particular webpage
2. HEAD: This is used to retreive the the head section of an HTTP request. This does not include the actual webcontent itself.
3. POST: This is used to send information to a server(uploading)
4. PUT
5. DELETE
6. OPTIONS
7. TRACE

## HTTP Response Status Codes
1. 1xx: Request Received and server processing
2. 2xx: Success
3. 3xx: Redirection
4. 4xx: Client Error
5. 5xx: Server Error

## `curl` command
The curl command is used for making requests to URLs. IP addresses can also be passed as argument to this command. Here are some useful flags:
* `-A`: Specify user agent
* `-b`: Pass the data to the HTTP server as a cookie
* `-d`: Sends specified data in a POST request
* `-D`: Write protocol specific headers to a specified file
* `-E`: Tell curl to use a particular certificate file
* `-L`: Redirection
* `-s`
* 

