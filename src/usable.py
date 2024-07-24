import re

def check_isolated_word(string, word):
    pattern = rf'(^|[^a-zA-Z]){word}([^a-zA-Z]|$)'
    return re.search(pattern, string) is not None

def check_isolated_letter(text, letter):
    
    allowed_surroundings = r'\s\.,;\/\\|\b'
    pattern = rf'(?<=[{allowed_surroundings}]){re.escape(letter)}(?=[{allowed_surroundings}])'
    matches = re.findall(pattern, text)
    
    return bool(matches)