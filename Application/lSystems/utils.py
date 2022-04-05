from .structure import Element_sequence
from .structure import Element

def string_to_element_sequence(string, default):
    es = Element_sequence()
    for c in string:
        es.append(Element(c, default))
    return es

def format_re_write_rules(re_write_rules, default):
    keys = list(re_write_rules.keys())
    for key in keys:
        key_ = Element(key, default) # Cria um elemento com o caractere
        re_write_rules[key_.content] = re_write_rules[key] # Adiciona a regra de produção com base no objeto key_
        
        if key_.content != key: # Se o caractere for diferente do caractere original
            del re_write_rules[key] # Remove a regra de produção original

        re_write_rules[key_.content]['r'] = string_to_element_sequence(re_write_rules[key_.content]['r'], default)

    return re_write_rules