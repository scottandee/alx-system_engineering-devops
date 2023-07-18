# 0x06 - REGULAR EXPRESSIONS

## What are Regular Expressions?
Regular expressions are a powerful and versatile tool to search, find and manipulate text strings. It is simply a sequence of characters that form a search pattern.

## Elements of Regular Expressions
1. Literals: These are regular expressions that match themselves
2. Repitition Tokens/ Greedy Quantifiers: This specifies the number of occurences of characters specifies
    * asterisk(`*`) : This match zero or more occurence of a token
    * plus(`+`) : This mathes one or more occurence of a token
    * dot(`.`) : This matches any singe character apart from a newline
    * question mark(`?`): This matches zero or one occurence of a character
    * curly brackets(`{}`) : Match exact occurences of a charcter or token
3. Anchor Token: This is used to specify where a pattern is to be found in text
    * `^` : This matches the position at the start of a line
    * `$` : This matches the position at the end of a line
    * `\A` : This matches the position at the start of a string
    * `\Z` : This matches the position at the end of a string
4. Character Token
    * `[0-9A-Za-z]` : This matches one out of several characters
    * `[^0-9A-Za-z]` : This matches characters that are not part of the list specified
    * `[a-zA-Z0-9]+` : This matches one or more of these characters specified
    * `[1st - [2nd]]` : This matches any one character in the first list but not in the second list
5. Non-Greedy/Lazy Quantifiers: This matches as little text as possible while still allowing the overall pattern to match successfully. They are denoted by adding `?` after the regular quantifier. eg `*?`, `+?`, `??`, `{n,}?`, `{n,m}?` 
6. Possessive Quantifier: These matches as much text as possile but do not backtrack to find alternative matches. They are denoted by adding a `+` after the regular quantifier. eg `*+`, `++`, `?+`, `{n,}+`, `{n,m}+`
7. Alternation (pipe`|`) : This acts like an OR operator. Matches any single one of the many regexes. It has the lowest precedence aming all reexp operators
