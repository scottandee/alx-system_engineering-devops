# 0x02 - SHELL I/O REDIRECTIONS AND FILTERS
Normally, the results to the commands we enter into the terminal is displayed on the standard output. We can redirect that output into a file, another command or even to the standard error. Filters are commands that help to remove unwanted parts of the results we get from the shell.
## What is the Standard Input?
This is a place where commands take their input. This is usually the keyboard but can be redirected to come from various other forms. It's referred to as the **stdin**
Here, we're sending the lines of the file as input to a command

```bash
sort < file.txt
```

We can also create a *here-document* with the `<<` redirection. This allows us to specify multiple lines of input directly within a script or command without the need for a separate input document

```bash
command << EOF
line 1
line 2
line 3
EOF
```
One major difference between the here-string and the here document is that the here string is read by the shell as one string rather than multiple lines of input

**NOTE**: The lines between EOF and EOF will be passed as input to the command. You can use any other marker, it just has to be uniform at the beginning and at the end

Additionally, we can create a *here-string* with the `<<<` redirection. This is is used to pass a single string as an input to a command. Its the shorthand for echoing a string and redirecting it as input

```bash
command <<< "input_string"
```
A here string can also can also be used in the form of an opening and closing single quote. It allows us the ability to specify a multiline input to a particular command like the previous methods we've described in this section.

```bash
command 'line 1
line 2
line 3'
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
Pipelines serve the purpose of passing the output of one command as the input of another command

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
5. `rev` : Reverse words
6. `cut` : Trim output. For more click [here](https://www.geeksforgeeks.org/cut-command-linux-examples/#:~:text=The%20cut%20command%20in%20UNIX,line%20and%20extracts%20the%20text.)

## Special Characters
[click here](http://mywiki.wooledge.org/BashGuide/SpecialCharacters)

## More
do `man 5 passwd`

## AUTHOR
* Olayinkascott Andee (andeeolayinkascott@gmail.com)
