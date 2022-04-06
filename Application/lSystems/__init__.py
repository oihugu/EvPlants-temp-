from Application.lSystems.structure import element_sequence
from Application.lSystems.structure.line import Linha
from . utils import *
from .structure import Element
from .. import utils
from . import structure


class L_system():

    __default = {'visual' :{'size': 1, 
                            'width': 1, 
                            'color': '#000000'},
                'space'   :{'position': (0,0),
                            'angle': 90,
                            'angle_diff': 33},
                'canvas'  :{'width': 1000,
                            'height': 1000}
                }

    def __init__(self, initial_string, re_write_rules, default = __default):
        '''
        re_write_rules - dicionário com as regras de produção para cada simbolo, podendo conter também, cor, tamanho, grossura da linha e diferença de ângulo
        O caractere padrão para o desenho de uma linha é "F"
        '''
        self.actual = {key: utils.general.complete_dictionary(value, self.__default[key]) for key, value in zip(default.keys(), default.values())} # Completa o dicionário de configurações default
        self.re_write_rules = format_re_write_rules(re_write_rules, self.actual)


        self.angle_operations = {
            '+' : self.rotate_right,
            '-' : self.rotate_left,
        }
        self.position_operators = {
            'F' : ''
        }
        self.storage_operators = {
            '[' : ']',
        }

        self.element_sequece = self.compose_element_sequence(initial_string)
        self.stack_store = []
        self.canvas = structure.Canvas(self.actual['canvas']['width'], self.actual['canvas']['height'])
            
    def compose_element_sequence(self, initial_string):
        es = Element_sequence()
        for i, c in enumerate(initial_string):
            es.append(Element(c, self.actual))
        return es
    
    def compile_element_sequence(self, idx, sequence, angle, position):
        if idx > len(sequence) - 1:
            return

        else:
            elem = sequence[idx]
        
        if elem.content in self.angle_operations.keys():
            angle_diff = self.angle_operations[elem.content](idx, angle)
            return self.compile_element_sequence(idx + 1, sequence, self.actual['space']['angle'] + angle_diff, position)
        
        elif elem.content in self.position_operators.keys():
            l = Linha(position, angle, self.actual['visual']['size'], self.actual['visual']['width'], self.actual['visual']['color'])
            self.canvas.draw_line(l)
            return self.compile_element_sequence(idx + 1, sequence, angle, l.end_position)

        elif elem.content in self.storage_operators.keys():
            return_point = sequence[idx:].find(Element(self.storage_operators[elem.content], self.actual))
            self.compile_element_sequence(idx + 1, sequence[:return_point], angle, position)
            return self.compile_element_sequence(idx + return_point + 1, sequence, angle, position)

                
    def rotate_right(self, idx, accumulator = 0):
        if self.element_sequece[idx] == Element('+', self.actual):
            return self.rotate_right(idx + 1, accumulator + 1)
        else:
            return accumulator * self.actual['space']['angle_diff']
    
    def rotate_left(self, idx, accumulator = 0):
        if self.element_sequece[idx] == Element('-', self.actual):
            return self.rotate_right(idx + 1, accumulator + 1)
        else:
            return -accumulator * self.actual['space']['angle_diff']
    
    def run_generation(self):
        self.zero_state()
        self.compile_element_sequence(0, self.element_sequece, 90, (0,0))
        
    def re_write(self):
        for replacer in self.re_write_rules.keys():
            elem = Element(replacer, self.actual)
            self.element_sequece.replace(elem, self.re_write_rules[replacer]["r"])
    
    def run(self, generations):
        for i in range(generations - 1):
            self.run_generation()
        self.run_generation()
        return self.canvas.plot()
    
    def zero_state(self):
        self.actual = self.__default
        self.canvas = structure.Canvas(self.actual['canvas']['width'], self.actual['canvas']['height'])
        self.idx_dct = {}
