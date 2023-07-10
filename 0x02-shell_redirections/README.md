# 0x02 - SHELL I/O REDIRECTIONS AND FILTERS
Normally, the results to the commands we enter into the terminal is displayed on the standard output. We can redirect that output into a file, another command or even to the standard error. Filters are commands that help to remove unwanted parts of the results we get from the shell.
## What is the Standard Input?
This is a place where commands take their input. This is usually the keyboard but can be redirected to come from various other forms. It's referred to as the **stdin**
```bash
sort < file.txt
```
## What is the Standard Output?
This is a place where commands display their output. This can also be rediirected. It's referred to as the **stdout**
```bash
ls -l > file.txt
```
To append to a file:
```bash
ls -l >> file.txt
```
Stdin from file.txt, stdout to sorted.txt:
```bash
sort < file.txt > sorted.txt
```
### What are Pipelines Used for?
Pipelines serve the purpose of passing the output of one command as the inout of another command

## Shell Filters
1. `sort` : This takes in input from the stdin and outputs the sorted output to stdout
2. `uniq` : This removes duplicate lines
3. `grep` : This outputs lines that match a particular pattern
4. `fmt` : This takes input from stdin and prints that input on the stdout
5. `pr` : This takes input from stdin and prints the output as if it were to be printed out.
6. `tr` : This deletes or removes part of the input from std in and prints to stdout
7. `sed` : This can perform more sophisticated text translations
8. `head` : output the first ten lines
9. `tail` : output the last ten lines
10. `awk` : This is an entire programming language for filtering

## Others
1. `echo` : This allows you to display whatever is passed as argument to stdout
    * -n : suppress new line character
    * -e : enable special characters(escaped characters)
2. `wc` : This counts words, lines or characters
3. `cat` : This concatenates and displays two files
    If no command is passed, cat reads from stdin
    ```bash
    cat > file.txt
    cat >> file.txt
    ```
4. `rev` : Reverse words
5. `cut` : Trim output. For more click [here](https://www.geeksforgeeks.org/cut-command-linux-examples/#:~:text=The%20cut%20command%20in%20UNIX,line%20and%20extracts%20the%20text.)

## Special Characters
[click here](http://mywiki.wooledge.org/BashGuide/SpecialCharacters)

## More
do `man 5 passwd`

## AUTHOR
* Olayinkascott Andee (andeeolayinkascott@gmail.com)
