import matplotlib.pyplot as plt

class Canvas():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.lines = []
    
    def add_line(self, linha):
        if self.lines == []:
            linha.start_position = (0,0)
        else:
            linha.start_position = self.lines[-1].end_position
        linha.end_position = linha.start_position + linha.rotate()
        self.lines.append(linha)

    def draw(self):
        plt.figure(figsize=(500, 500))
        for line in self.lines:
            plt.plot(line.start_position, line.end_position, color = line.color, linewidth = line.width)
        return plt