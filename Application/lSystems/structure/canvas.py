import numpy as np
import matplotlib.pyplot as plt

class Canvas():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.lines = []
    
    def add_line(self, linha, idx = -1, stack = []):

        self.lines.append(linha)
        print(self.lines)

    def draw(self):
        plt.figure(figsize=(5, 5))
        for line in self.lines:
            line.plot()
        return plt