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
        self.default = {key: utils.general.complete_dictionary(value, self.__default[key]) for key, value in zip(default.keys(), default.values())} # Completa o dicionário de configurações default
        self.re_write_rules = format_re_write_rules(re_write_rules, self.default)
        self.lines = []


        self.angle_operations = {
            '+' : self.rotate_right,
            '-' : self.rotate_left,
        }
        self.position_operators = {
            'F' : self.draw_segment
        }
        self.storage_operators = {
            '[' : self.store_state,
            ']' : self.return_state
        }

        self.element_sequece = self.compose_element_sequence(initial_string)
        self.stack_store = []
        self.stack_send = []

            
    def compose_element_sequence(self, initial_string):
        es = Element_sequence()
        for i, c in enumerate(initial_string):
            es.append(Element(c, self.default))
        return es
    
    def compile_element_sequence(self):
        self.zero_state()
        
        for i, element in enumerate(self.element_sequece):
            if element.content in self.angle_operations:
                self.angle_operations[element.content](i)
                
            if element.content in self.position_operators:
                self.idx_dct[i] = self.position_operators[element.content](i)
                
            if element.content in self.storage_operators:
                self.storage_operators[element.content](i)

                
    def rotate_right(self, idx, accumulator = 0):
        if self.element_sequece[idx] == Element('+', self.default):
            return self.rotate_right(idx + 1, accumulator + 1)
        else:
            self.element_sequece[idx].angle += accumulator * self.default['space']['angle_diff']
    
    def rotate_left(self, idx, accumulator = 0):
        if self.element_sequece[idx] == Element('-', self.default):
            return self.rotate_right(idx + 1, accumulator + 1)
        else:
            self.element_sequece[idx].angle -= accumulator * self.default['space']['angle_diff']

    def draw_segment(self, idx):
        if self.lines == []:
            start = [0,0]
            print(f'1. Começando')
            
        elif (self.stack_send != []) and (idx == self.stack_send[-1]):
            idx_act, idx_store = self.stack_send.pop()
            start = self.lines[self.idx_dct[idx_store]]
            print(f'2. Retriving Stored -> {start}')
            
        else:
            start = self.lines[-1].end_position
            print(f'3. Retriving -> {start}')
            
        self.lines.append(Linha(start,
                                self.element_sequece[idx].get_angle(), 
                                self.element_sequece[idx].get_size(),
                                self.element_sequece[idx].get_width(),
                                self.element_sequece[idx].get_color()))
        
        return len(self.lines) - 1

    def store_state(self, idx):
        self.stack_store.append(idx)

    def return_state(self, idx):
        print(f'## stack_store -> {self.stack_store}')
        self.stack_send.append((idx, self.stack_store.pop()))
    
    def run_generation(self):
        self.re_write()
        self.compile_element_sequence()
        
    def re_write(self):
        for replacer in self.re_write_rules.keys():
            elem = Element(replacer, self.default)
            self.element_sequece.replace(elem, self.re_write_rules[replacer]["r"])
    
    def run(self, generations):
        for i in range(generations - 1):
            self.run_generation()
        self.run_generation()
        canvas = structure.Canvas(self.default['canvas']['width'], self.default['canvas']['height'], self.lines)
        plt = canvas.draw()
        return plt
    
    def zero_state(self):
        self.lines = []
        self.stack_send = []
        self.stack_store = []
        self.idx_dct = {}
        
    '''def add_line(self, linha, idx = -1, stack = []):
        if self.lines == []:
            linha.start_position = (0,0)
        elif idx == stack.top():
            linha.start_position = self.lines[stack.pop()].end_position
        else:
            linha.start_position = self.lines[idx].end_position
        
        linha.end_position =  linha.new_end(linha.start_position)'''
    
    '''def draw_sequence(self, canvas):
        for line in self.lines:
            canvas.add_line(line)'''