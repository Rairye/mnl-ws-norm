# mnl-ws-norm
Light-weight tool for normalizing whitespace and accurately tokenizing words. Multiple natural languages supported. Useful for scrapping, machine learning, and data analysis.

## Installation

## Background

A person experience led me to realize the possible shortcomings of solely relying on regex and the split method.

I was analyzing text taken from public domain material that had been written by multiple authors. When I used the split method to tokenize the words, I had noticed that the words in the document had not been split individually. (Instead, some of the elements in the list were strings of multiple words.)

Upon investigation, I had discovered that some of the space characters, despite looking the same to me, had different Unicode values. This meant that Python did not identify them as being the same, and thus the split method produced unexpected results.

My solution was to write a script for normalizing spaces in the document, and, thankfully, I have not had the same problem since then.
