# 0x00 - SHELL BASICS
In this project, we go over basic shell commands for navigation, looking around, manipulating files and working with commands

## What is the Shell?
The shell is a tool that acts as an intermediary in between the keyboard and the OS. It's main function is to interpret the commands we enter into our **terminal** to the OS
## What is a Terminal?
This is actually called a terminal emulator. The terminal serves as the interface for the shell

## Some Common Commands and their Uses
1. `pwd` : This is used to print the present working directory.
2. `cd` : This is used to change our present working directory into another one
3. `ls` : This is used to list ou all the contents of the directory specified. If none is specified, it'll list out the contents of our present working directory
   * -a : all files including hidden files
   * -l : long list format
   * -t : sort by time modified
   * -s : sort by size
4. `less` : This lets us view text files
5. `file` : this command tells us the type of file that is passed as argument
6. `cp` : copy files and directories
7. `mv` : move or rename files
8. `rm` : delete files
    * -r : remove recursively
    * -f : force remove
    * -d : remove empty directories
9. `mkdir` : this is used to create a new directory
    * -m : used to set file mode
    * -p : no error if existing, create parent directory as necessary
10. `type`: display information abou the type of a command
11. `man`: on-line help page
12. `which` : display the location of a command
13. `help` : reference page for shell buitin
14. `ln` : This creates a link between files
    * Hard link: This creates multiple entry points into the same file.

      ```bash
      ln <original_file> <link_name>
      ```
    * Symbolic link: This creates a shortcut to a particular file

      ```bash
      ln -s <target or original file> <link_name>
      ```
  ## A Guided Tour
  * `/` : root directory. This is the top level directory
  * `/boot` : contains files for booting the machine
  *  `/etc` : this contains the configuration files for the system. (/etc/passwd for passwords, /etc/hosts for ip and hostnames config)
  *  `/bin` : binary files dir. Contains program executables
  *  `/usr/bin` : apps for the system user
  *  `/sbin`, `/usr/sbin` :
  *  `/usr` :
  *  `/var` :
  *  `/lib` :
  *  `/tmp` :
  *  `/dev` :
  *  `/media` :
  *  `/proc` :


## Note
* `~` on the command line refers to the home directory
