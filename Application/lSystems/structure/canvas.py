import numpy as np
import matplotlib.pyplot as plt

class Canvas():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.fig = plt.figure(figsize=(5, 5))
    
    def add_line(self, linha, idx = -1, stack = []):
        self.lines.append(linha)

    def draw_line(self, line):
        line.plot()
    
    def plot(self):
        plt.show()
