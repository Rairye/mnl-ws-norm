# mnl-ws-norm
Light-weight tool for normalizing whitespace and accurately tokenizing words. Multiple natural languages supported. Useful for scrapping, machine learning, and data analysis.

## Installation

## Background

A personal experience led me to realize the possible shortcomings of solely relying on regex and the split method in Python.

I was analyzing text data taken from public domain material that had been written by multiple authors. When I used the split method to tokenize the words by half-width space, I had noticed that the words were not split individually; instead, some of the elements in the result list were strings made up of multiple words.

Upon investigation, I had discovered that some of the space characters, despite looking the same to me, had different Unicode values. This meant that Python did not identify them as being the same, and thus the split method produced unexpected results.

My solution was to write a script for normalizing spaces in the document, and, thankfully, I have not had the same problem since then.

## Splitting (Tokenization)

One common way to split (tokenize) strings into individual words (such as in English) in Python is to use the split method; for example -> words_list = “This is my sentence”.split(“ “)

The split method is convenient and easy when only one type of space is used in the text. In the above example, a half-width space is used to split “This is my sentence.” into a list where each element contains only one word.

However, there may be cases where you need to split words from text data where multiple types of spaces (or other whitespace characters) are used. This could be text sources written by multiple authors or text from the Internet (such as customer reviews or social media posts). This may also happen in text that was converted from an image or PDF using OCR.

Also, whitespace characters are not limited to spaces; tabs and new line characters also count as whitespace characters. This is further complicated by the fact that there are multiple types of spaces, tabs, and new line characters. (For a list of whitespace characters and their Unicode values, please see https://en.wikipedia.org/wiki/Whitespace_character)

### Code Examples

split_by_spaces(input_str)

input_str is the string from which words are to be tokenized. 

input_str must be passed as a str type.

```python

from mnl_ws_norm.normalizer import split_by_spaces

#Source string 1 with half-width spaces (Unicode: U+0020) and a tab (Unicode: U+0009).
source_str1 = "Hey, everybody,  how are you doing?"

#Source string 2 with half-width spaces and a \n character (Unicode: U+000A).
source_str2 = "Hey, everybody\nhow are you doing?"

#Source string 3 with half-width spaces and a full-width space (Unicode: U+3000).
source_str3 = "Hey, everybody,	how are you doing?"

print("source_str1: {}".format(split_by_spaces(source_str1)))
print("source_str2: {}".format(split_by_spaces(source_str2)))
print("source_str3: {}".format(split_by_spaces(source_str3)))

#There may be some cases where you want to split a string into lines and then split those lines by whitespace character.
#In such a case, you can use the splitlines() method.

source_str = "Hey, everybody.\nHow are you doing?\rI am alright."

line_list = source_str.splitlines()

for i in range(len(line_list)):
	print("Line {}: ".format(i) + str(split_by_spaces(line_list[i])))

```

## Normalizing

In Python, regular expressions can be used to normalize whitespace characters (change certain whitespace characters into other characters). It is relatively easy to write code to normalize a specific whitespace character, but it becomes complicated if you would like to normalize all whitespace characters. Thankfully, there is a simple solution.

### Code Examples

norm_spaces(input_str, space_type, remove_extra_spaces = False)

Required arguments -> input_str, space_type

input_str is the string in which the whitespace characters are to be replaced.

input_str must be passed as a str type.

space_type is the string used to replace all whitespace characters in input_str.

space_type must be passed as a str type.

Optional argument -> remove_extra_spaces

By default, extra whitespace characters are not removed from input_str. 

Specifying remove_extra_spaces as True removes extra whitespace characters from input_str.

Note: Regardless of the value of remove_extra_spaces, the returned string may have leading/trailing whitespace characters, so you may want to use the strip() method as necessary.

```python

from mnl_ws_norm.normalizer import norm_spaces

#Source string with consecutive half-width spaces (Unicode: U+0020) and a tab (Unicode: U+0009).
source_str = "  Hey,  everybody, 	how  are  you  doing?  "

#Spaces in source_str are replaced with a half-width space, while extra spaces are ignored.
print(norm_spaces(source_str, " "))

#Spaces in source_str are replaced with a half-width space, and extra spaces are removed.
print(norm_spaces(source_str, " ", True))

#Spaces in source_str are replaced with a full-width space, while extra spaces are ignored.
print(norm_spaces(source_str, "　"))

#Spaces in source_str are replaced with a full-width space (Unicode: U+3000), and extra spaces are removed.
print(norm_spaces(source_str, " 　", True))

```
