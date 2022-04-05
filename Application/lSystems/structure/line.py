import numpy as np
import matplotlib.pyplot as plt

class Linha():
    
    def __init__(self, angle, size, width, color = (0,0,0)):
        self.angle = angle
        self.start_position = None # x0,y0
        self.end_position = None # x1,y1
        self.size = size
        self.width = width
        self.color = color
    
    def rotate(self):
        theta = np.radians(self.angle)
        c, s = np.cos(theta), np.sin(theta)
        R = np.array(((c, -s), (s, c)))
        return R.dot(np.array([self.size,0]))

    def __str__(self) -> str:
        return f"Linha(pos=({self.start_position}, {self.end_position}), angle={self.angle}, size={self.size}, width={self.width}, color={self.color})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def plot(self):
        plt.plot([self.start_position[0], self.end_position[0]],
                    [self.start_position[1], self.end_position[1]],
                    color = self.color, linewidth = self.width) # [x0,x1], [y0,y1]

    def new_end(self, start):
        self.end_position = self.rotate() + (np.array([0,self.size]) + start)
        return self.end_position
