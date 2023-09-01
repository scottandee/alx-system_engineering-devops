# 0x03 - SHELL, INIT FILES, VARIABLES AND EXPANSIONS

## What are Expansions?
Expansions are the series of processes that are performed on commands that are entered into the terminal. This expansion is usualy done by the shell

### Types of Expansion
1. Pathname Expansion : This expands [wildcards](http://mywiki.wooledge.org/BashGuide/SpecialCharacters)
3. Tilde Expansion(~) : This expands to the home directory
4. Arithmetic Expansion : This performs arithmetic by expansion
   
   ```bash
   $((expression))
   ```
6. Brace Expansion : This is used to create multiple text strings from a specified pattern

   ```bash
   $ echo mail-{a,b,c}
   mail-a mail-b mail-c
   $ echo {1..9}
   1 2 3 4 5 6 7 8 9
   $ echo {a-i}
   a b c d e f g h i
   ```
   What would this result into?
   
   ```bash
   $ echo {2025..2026}-{01..12}
   ```
8. Command substitution : This can be used then you want to substitute for the output of a command as an expansion

    ```bash
    $ echo $(ls)
    Documents Home Pictures Recycle_Bin Videos
    ```
10. Parameter Expansion : This is used for expanding variables

    ```bash
    $ NAME="Andee"
    $ echo "$NAME"
    Andee
    ```
12. Quoting : There are two phases to this
    * **Double Quotes**: When text is wrapped around double quotes, all special characters loose their meaning apart fom the dollar sign, backticks  and the forward slash. That means that in the double quote, word-splitting, Tilde, Pathname, and Brace expansion are suppressed but Arithmetic, Command substitution, parameter expansion are active.

      Example of word-splitting:
        ```bash
        $ ls -l two words
        ls: cannot access two: No such file or directory
        ls: cannot access words.txt: No such file or directory
        $ ls -l "two words"
        -rw-rw-r-- 1 me me 18 2020-02-20 13:03 two words
    * **Single Quotes** : This prevents all form of expansions 
14. Escape Characters : To use special characters as text, we have to escape it with a forward slash

## Shell Variables

### Global Variables
Global variables or Environment variables are variables that are avaliable to all shells. It is usually accessed by typing in the `printenv` or `env` command

### Local Variables
Local variables are variables that are only avaliable to the current running shell. It is usually accessed by typing in the `set` command which shows all the variables avaliable including environment variables.

### Useful Commands
1. `set` : To list out all local and environment variables if no arguments are passed. If a parameter and value is passed it is set locally
2. `unset` : This is used to remove a variable from existence
3. `readonly` : this is used  to specify a rule that one set, it cannot be reassigned
4. `export` : This is used to make a local variable an environment variable. It can be done on one line.

   **Note**: You can make changes to a an environment variable on your current shell but it won't affect the parent
### Some Special characters
1. `$1, $2,...` : These are for command line arguments
2. `$@` : Expands to cmd line args starting from 1
3. `$#` : Number of cmd line args
4. `$$` : process id of the shell
5. `$?` : Exit status of the previous command
6. `$0` : Name if the shell script

## Shell Init Files
In linux, there are two major classifications of shell initialization files. They are:
1. System profile files
2. User profile files

### What are System Profile Files?
Sytem profile files are files that permanently set the variables, functions and aliases globally for the entire system. Simply, they set environment variables.
These files are usually run when a user logs in.

* **/etc/profile**: This file is used to set environment variables, functions and aliases globally for the entire system. This file also contains references to other files (e.g /etc/inputrc, /etc/profile.d). This file belongs to the root user and can only be edited by the root user. On machines that can run multiple shells, this file is sourced by the different shell programs. This is the reason why shell specific configurations are not put in this file but in some other files

* **/etc/bashrc**: This file contains shell specific system profle configurations. It sets the variables, fuctions and aliases globally for a specific shell

### What are User Profile files
These are files that set the functions, variables and aliases for each user. These files are usually copied from the **/etc/skel/** directory. The user profile files are usually contained in the user home directory. Once these files are edited/appended, changes will be enabled only after the user logs out and logs back in hence, emphasizing the *"initialization"* file purpose

* **~/.bash_profile**: This file is usually run as a user logs in. It is the preferred file for setting user configurations
* **~/.bash_login**: This file contains configurations that are usually executed when you log in to your machine
* **~/.profile**: In the absence of **~/.bash_login** and **~/.bash_profile**, this file is usually sourced
* **~/.bashrc**: This is used to configure the bahaviour of a bash shell for a specific user. It is usually read as the user logs in interactively. This file usually references the **/etc/bashrc** file
* **~/.bash_logout**: This contains specific instructions about the logout procedure
* **~/.bash_history**: This contains the command line history of the user


## `alias` Command
This is used to give another name to a particular command. This is usually temporary but can be made permanent by setting it in the **~/.bashrc** file

To set an alias:
```bash
alias new_command="old_command"
```
To Unset an alias:
```bash
unalias alias_name
```
## `source` and `.` Commands
The source and dot commands are used to execute command from a file in the current shell. Both commands perform the same action. One of them is just the shorthand.

```bash
$ source /path/to_script
$ . /path/to_script
```

## `printf`
This prints a formatted output. It's pretty similar to the printf function in C

```bash
printf [FORMAT] [ARGUMENTS]...
```

```bash
printf "Name: %s\n" $NAME
```

## AUTHOR
* Olayinkascott Andee (andeeolayinkascott@gmail.com)
