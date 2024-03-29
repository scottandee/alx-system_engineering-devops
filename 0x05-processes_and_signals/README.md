# 0x05 - PROCESSES AND SIGNALS
The aim of this project is to learn:
* About processes and the process identification number
* The various ways view and monitor and manage the processes on the command line interface
* About the types of signals that exist and how they can be used to manage processes

## What is a Process?
A process is a running/executing instance of a program. Each process has a unique PID(Process Identification Number) which is always a non negative integer. A very large PID doesn't mean that there are a lot of processes running, these numbers are not usually reused to avoid errors.

The default maximum number of PIDs is 32,767. It's essentially the maximum number of processes that can exist simultaneously on a system. The lower the maximum values, the sooner the values will wrap around. The pid_max file is a file that specifies the value that the PIDs wrap around. It has a default PID of 32,768 but it can be set to any value up to approximately 4 million.The maximum number of processes running in a machine is onky limited to the amount of RAM it possesses.

The init process is the only one that has a constant process id. It is the parent of all other processes.

## Types of Processes
* Foreground Processes : This is a process that depends on a user for input. They are called interactive processes
* Background Processes : These are processes that run independently of the user. They are called non-interactive processes

## Process States in Linux
* Running (R) : This is when the process is active and is already making use of the system resources to perform its action
* Sleeping (S) : This is when the process is waiting for a particular resource to be avaliable to it. A process in **interruptible** sleep will wake up to handle signals but a process in **non-interuptible**(D) sleep wont wake up.
* Stopped (T) : A process enters the stopped state when receives a stop signal
* Zombie (Z) : The process is dead but still has an entry on the process table

## Commands for Managing Processes
1. `pkill` : This is used to interrupt a running process. This is used to send a signal to a process based on their names or other attributes(pattern).
2. `top` : This displays all current runnung processes. This returns data in realtime
3. `kill` : This command is used to stop a running process. This is used to send a signal to a process based on their pid
4. `ps` : This shows a snapshot of the current running processes
5. `pgrep` : List pids of processes that match a given pattern
6. `trap` : This is used to specify a particular outcome if a signal is detected
7. `pidof` : This is used to display the pidof a particular process
8. `pstree` : This is used to display the tree of all processes
9. `exit` : This command causes normal process termination

## The `/proc` Filesystem
This is where information on the current running process is stored. This filesystem conntains kernel data that changes in real time. If you list the files in the /proc, youll notice that there are numbered directory corresponding to each running process.

## What is a Signal
This is an event generated by the LINUX system in response to some condition. Some of the LINUX signals are:

* SIGHUP : Sent to indicte that the terminal session has been disconnected
* SIGINT : Sent when a user enters Ctrl + C
* SIGKILL : Quit immediately
* SIGQUIT : Sent when a user enters Ctrl + D
* SIGTERM : Used to request termination of a process
* SIGFPE : This is sent when an illegal mathematical operation is performed

## The `tee` Command
This is a command that reads from **stdin** and writes to both **stdout** and one or more files. We can redirect the output to stdout to `/dev/null` if it's not needed

```bash
echo Hi | tee my_txt_file.txt > /dev/null
```

## AUTHOR
* Olayinkascott Andee (andeeolayinkascott@gmail.com)
