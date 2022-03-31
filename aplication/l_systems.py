import matplotlib.pyplot as plt
import numpy as np
import chart_studio
import os
from . import utils



    # Setters
    def zero_state(self):
        self.angle = 90
        self.angle_diff = 33

    def set_color(self, color):
        self.color = color
    
    def set_width(self, width):
        self.width = width
        
    def store_state(self):
        self.stack_pos.add(self.position)
        self.stack_angle.add(self.angle)
            
    def return_state(self):
        self.position = self.stack_pos.remove()
        self.angle = self.stack_angle.remove()
        

    #Step
    def step(self):
        self.width, self.color = self.d_width, self.d_color
        self.position = (0,0)
        self.lines = []
        
        for sub_string in self.re_write_rules.keys():
            self.string = self.string.replace(sub_string, self.re_write_rules[sub_string]['r'])
        
        for carac in self.string:
            carac = str(carac)
            if carac in self.angle_operations.keys():
                self.angle = self.angle_operations[carac](self)

            elif carac in self.position_operators.keys():
                self.position_operators[carac]()

            elif carac in self.storage_operators.keys():
                self.storage_operators[carac]()
        

    # Geometry
    def rotate(self):
        theta = np.radians(self.angle - 90)
        c, s = np.cos(theta), np.sin(theta)
        R = np.array(((c, -s), (s, c)))
        return R.dot(np.array([self.size,0]))

    def draw_segment(self):
        self.lines.append(Linha(self.position,
                                self.position + self.rotate(),
                                self.size,
                                self.width,
                                self.color))
        self.position = self.position + self.rotate()


    # Vizualization
    

    
    # Utils
    def compose_string(self, string, re_write_rules):
        flag = False

        ls = utils.List_of_chars([])

        for c in string:
            char = utils.general.get_char(c, self.default, re_write_rules)
            ls.append(char)
            
            if flag and not(char in (self.angle_operations)):
                self.zero_state()
                flag = False

            elif char in (self.angle_operations):
                flag = True
        
        return ls
            

        
