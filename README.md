# mnl-ws-norm
Light-weight tool for normalizing whitespace and accurately tokenizing words. Multiple natural languages supported. Useful for scrapping, machine learning, and data analysis.

## Installation

## Background

A person experience led me to realize the possible shortcomings of solely relying on regex and the split method in Python.

I was analyzing text data taken from public domain material that had been written by multiple authors. When I used the split method to tokenize the words by half-width space, I had noticed that the words were not split individually; instead, some of the elements in the result list were strings made up of multiple words.

Upon investigation, I had discovered that some of the space characters, despite looking the same to me, had different Unicode values. This meant that Python did not identify them as being the same, and thus the split method produced unexpected results.

My solution was to write a script for normalizing spaces in the document, and, thankfully, I have not had the same problem since then.

## Splitting (Tokenization)

One common way to split (tokenize) strings into individual words (such as in English) in Python is to use the split method; for example -> words_list = “This is my sentence”.split(“ “)

The split method is convenient and easy when only one type of space is used in the text. In the above example, a half-width space is used to split “This is my sentence.” into a list where each element contains only one word.
