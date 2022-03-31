import os
from . import list_of_chars
from .char import Character

def string_to_list_of_chars(string, default):
    return list_of_chars.List_of_chars(Character(c, default) for c in string)

def format_re_write_rules(re_write_rules, default):
    keys = list(re_write_rules.keys())
    for key in keys:
        key_ = Character(key, default)
        re_write_rules[key_] = re_write_rules[key]
        del re_write_rules[key]
        re_write_rules[key_]['r'] = string_to_list_of_chars(re_write_rules[key_]['r'], default)
    print(re_write_rules)
    return re_write_rules

def get_char(char, default, re_write_rules):
    return Character(char,
                      default,
                      re_write_rules.get('size'),
                      re_write_rules.get('width'), 
                      re_write_rules.get('color'), 
                      re_write_rules.get('angle_diff'))

def verify_or_create_folder(folder):
    if not os.path.exists(f'output/{folder}'):
        os.makedirs(f'output/{folder}')