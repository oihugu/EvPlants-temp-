from .. import utils
from . import structure


class L_system():

    def __init__(self, initial_string, re_write_rules, size = 1, width = 1, color = '#000000'):
        '''
        re_write_rules - dicionário com as regras de produção para cada simbolo, podendo conter também, cor, tamanho, grossura da linha e diferença de ângulo
        symbols - lista de simbolos que não serão ignorados pelo programa
        O caractere padrão para o desenho de uma linha é "F"
        '''
        self.d_position, self.lines, self.angle, self.angle_diff = (0,0), [], 90, 33 
        self.size, self.d_width, self.d_color = size, width, color
        self.default = [self.size, self.d_width, self.d_color, self.angle_diff]
        self.re_write_rules = utils.general.format_re_write_rules(re_write_rules, self.default)
        self.stack_pos = utils.data_structures.Stack()
        self.stack_angle = utils.data_structures.Stack()
        self.angle_operations = {
            'C(+)' : lambda x : self.angle + self.angle_diff,
            'C(-)' : lambda x : self.angle - self.angle_diff
        }
        self.position_operators = {
            'C(F)' : self.draw_segment
        }
        self.storage_operators = {
            'C([)' : self.store_state,
            'C(])' : self.return_state
        }
        self.string = self.compose_string(initial_string, self.re_write_rules)
    