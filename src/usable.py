import re
import inspect

aboslute_path = "/Users/stefaniancu/Documents/VS Code/JobScraperEngine/"  #no idea why relative path with .. doesn't work

def check_isolated_word(string, word):
    pattern = rf'(^|[^a-zA-Z]){word}([^a-zA-Z]|$)'
    return re.search(pattern, string) is not None

def check_isolated_letter(text, letter):
    
    allowed_surroundings = r'\s\.,;\/\\|\b'
    pattern = rf'(?<=[{allowed_surroundings}]){re.escape(letter)}(?=[{allowed_surroundings}])'
    matches = re.findall(pattern, text)
    
    return bool(matches)

def get_variable_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    for var_name, var_val in callers_local_vars:
        if var_val is var:
            return var_name