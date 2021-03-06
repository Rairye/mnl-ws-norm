# mnl-ws-norm
Light-weight tool for normalizing whitespace and accurately tokenizing words (no regex). Multiple natural languages supported. Useful for scrapping, machine learning, and data analysis. 

## Installation

```python
pip install mnl-ws-norm
```

### Code Examples (Splitting)

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
### Code Examples (Normalization)

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
print(norm_spaces(source_str, "???"))

#Spaces in source_str are replaced with a full-width space (Unicode: U+3000), and extra spaces are removed.
print(norm_spaces(source_str, "???", True))

```

# Other languages

1. JavaScript -> https://github.com/Rairye/js-mnl-ws-norm

