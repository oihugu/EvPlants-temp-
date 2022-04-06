import numpy as np
import matplotlib.pyplot as plt

class Canvas():
    def __init__(self, width, height, lines):
        self.width = width
        self.height = height
        self.lines = lines
    
    def add_line(self, linha, idx = -1, stack = []):
        self.lines.append(linha)

    def draw(self):
        plt.figure(figsize=(5, 5))
        for line in self.lines:
            line.plot()
        return plt