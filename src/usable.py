import re

def check_isolated_word(string, word):
    pattern = rf'(^|[^a-zA-Z]){word}([^a-zA-Z]|$)'
    return re.search(pattern, string) is not None

def check_isolated_letter(string, letter):
    pattern = rf'(^|[^a-zA-Z]){letter}([^a-zA-Z]|$)'
    return re.search(pattern, string) is not None