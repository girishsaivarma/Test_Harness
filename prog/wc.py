import re

# Alternative wc.py logic using regular expressions

def count_lines(text):
    # Using regular expressions to count lines
    return len(re.findall(r'.+', text))

def count_words(text):
    # Using regular expressions to count words
    return len(re.findall(r'\w+', text))

def count_characters(text):
    # The character count does not change, as it is a direct count of string length
    return len(text)

def wc(text):
    num_lines = count_lines(text)
    num_words = count_words(text)
    num_characters = count_characters(text)
    
    return num_lines, num_words, num_characters

# Sample text to test the functions
sample_text = "Hello world!\nThis is a test text.\nIt has three lines and 13 words."

# Testing the rewritten functions
wc(sample_text)
