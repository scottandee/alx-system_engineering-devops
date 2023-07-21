# 0x0B - SSH
SSH stands for Secure Shell. The SSH protocol is used to establish encrypted connection between two devices. It is the primary means of connecting to linux servers remotely to make changes, execute commands, and configure other services remotely

In this project, we are given a server, `web-01` server to help us learn how to use ssh

## What is a Server?
A server is like a computer system that's on steroids. It's main purpose is to provide services and functionality to the clients.

## How SSH Works
First, we have to consider the two  types of encryption ie Symmetrical and Asymmetrical
1. **Symmetrical Encryption**: This is a type of encryption in which there's one shared key. Anyone who holds the key can encrypt messages and anyone else who holds the key can decrypt the message. Symmetric Encryption is what is used to encrypt the entire SSH connection. Public/private key is only used for authentication.
2. **Asymmetrical Encryption**: This is a type of encryption which involves two keys; A public key and a private key. Whatever is encrypted by the public key can only be decrypted by the private key. The public key can be shared to whoever but the private key must be kept private

The next major tool SSH uses is **Hashing**. Hashing is the process of converting data(passwords, credentials etc) into encrypted values that cannot be decrypted. The **hash function** is responsible for performing this encryption and the output is usually called the **hash value** or **digest**. The output of the hash function is the same for same inputs. If there is a slight change in the input, there'll be a mojor difference in the output function. Only the hash function can produce the correct hash value when it's given input. The main use for this in SSH is for hash-based message authentication codes(HMAC). It's basically just to check for data integrity and to verify the authenticity of communication.

As part of the symmetrical encryption a MAC is selected. Each message sent after this must contain a MAC so that the other party can verify the packet integrity. This is calculated from the shared key in the symmetrical encryption, the data itself and packet sequence number.

SSH works on a client-server model. The server must have an application called the ssh daemon which will listen for connections on a specific network port, authenticates connection requests and spawns the approprite environment if the user provides the correct credentials. The user computer must have an ssh client that knows how to communicate using the SSH protocol

## Generating SSH Keys
We do this with the `ssh-keygen` command

## References
* [Digital Ocean 1](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)
* [Digital Ocean 2](https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process)

## Author
* Olayinkascott Andee(andeeolayinkascott@gmail.com)
