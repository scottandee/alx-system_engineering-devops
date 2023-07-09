# 0x01 - SHELL PERMISSIONS
The UNIX operating system is a multi-user, multi-tasking machine. Therefore, different users can hava access to a particukar machine.
Shell permissions was made to bring order to the multi-user feature of the UNIX OS. Afterall, we won't one user tampering with another users files or one user crashing the entire machine.

## Some  Commands associated with file permissions
1. `chmod` : This is used to changed the permissions(access rights) of a file
    * Numeric Permissions
        * 0 - No permissions
        * 1 - Execute permissions
        * 2 - Write permission
        * 3 - Execute and Write permission
        * 4 - Read only permission
        * 5 - Read and execute
        * 6 - Read and write
        * 7 - Read, write, execute
    * Symbolic Permissions
        * u - user/owner
        * g - group
        * o - others
        * a - all
    * `-R` : This says that we want to give permissions recursively
    * Some Examples
         ```bash
         chmod u=rx, go=r my_file
         ```
         ```bash
         chmod -R u+x my_dir
         ```
         ```bash
         chmod 700 my_dir
         ```
2. `su` : This command is used ti switch user. Using this command without any username as argument will assume you want to log in as the root user
3. `sudo` : This command is used for executing commands as the root user
4. `chgrp` : This is used to change the group ownership of a file
5. `adduser`: This is used to add a new user to your machine
6. `whoami` : This will tell you who you're logged in as
7. `groups` : Print the groups a user is in

## AUTHOR
* Olayinkascott Andee(andeeolayinkascott@gmail.com)
