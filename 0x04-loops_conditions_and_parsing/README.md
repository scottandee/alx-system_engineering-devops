# 0x04 - LOOPS, CONDITIONALS AND PARSING
The project aim is to learn how to use loops (for, while, until), condition statements(if, else, elif, case), and various other commands that help to parse (cut command, file test operators, comparison operators) in shell scripting(bash).  
Here's a link to a [playlist](https://youtube.com/playlist?list=PLS1QulWo1RIYmaxcEqw5JhK3b-6rgdWO_) that explains most of these concepts in detail

## What is the advantage of using `#!/usr/bin/env bash` over `#!/bin/bash`
The advantage of using the #!/usr/bin/env bash shebang is that it adds portability to our script. Portability in the sense that our script can run on different types of machines without running into any error. Files are stored in different locations on different machines but the path to **env** which is `/usr/bin/env` is always the same on all flavours of linux. The **env** command has different uses, one of which is to run commands in a modified environment. WHen using the env command, it'll search through with the `PATH` variable for the file that we specify. It uses the first executable that appears first in the PATH variable

## Bash Loops

### While Loop
This loop is used to specify a condition for which must be passed for the loop to continue
Syntax:

```bash
while [ CONDITION ]; do COMMAND; done
while [ CONDITION ];
do
  COMMAND
done
```

Example:

```bash
n=1
while [ $n -le 5 ]
do
  echo $i
  n++
done
```
**NOTE**: Semicolon (;) in can be used to separate two commands that are to be executed one after the other and not togrther. That is;

```bash
$ echo $$
$ ls
$ echo $$; ls
```
### Until loop
The `until` loop is the opposite of the while loop. This loop specifies a condition for which the loop will be terminated. It has the same syntax with the while loop with the only two differences being the keyword `until` and the manner in which the condition is specified

### For Loop
This is used to iterate over a list of values

We can write it as a one liner:
```bash
for VARIABLE in LIST; do COMMANDS;done
```

Or write it expanded:
```bash
for VARIABLE in LIST
do
  COMMANDS
done
```

The different ways we can specify the list were going to iterate over are:
```bash
for i in 1 2 3 4 5 .. N , for command in ls pwd date
for i in {1..10}
for i in {1..10..2} - 1 is start, 2 is end, 2 is increment
for (( i=0; i<5; i++ ))
for i in "$LIST"
```

## Bash Conditionals (IF, ELIF, ELSE)
Syntax:

```bash
if [ CONDITION ]; then COMMAND; elif [ CONDITION ]; then COMMAND; else COMMAND; fi
if [ CONDITION ]
then
  COMMAND
elif [ CONDITION ]
then
  COMMAND
else
  COMMAND
fi
```

## Comparison Operators
For string comparisons
1. `=`: compare if two strings are equal i.e `if [ s1 = s2 ]`
2. `!=`: compare if two strings are not equal i.e `if [ s1 != s2 ]`
3. `-n`: evaluate if string length is greater than zero i.e `if [ -n s1 ]`
4. `-z`: evaluate if string length is equal to zero i.e `if [ -z s1 ]`
5.  `if [ s1 ]`: this returns true if s1 is not empty

For integer comparisons:
1. `-eq`: check if two numbers are equal
2. `-ge`: greater than or equal to
3. `-le`: less than or equal to
4. `-ne`: not equal to
5. `-gt`: greter than
6. `lt`: less than

## File Test Operators
For file test operators, here's a [link](https://tldp.org/LDP/abs/html/fto.html) to all of them.

## Author
* Olayinkascott Andee (andeeolayinkascott@gmail.com)
