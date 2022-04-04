import numpy as np

class Linha():
    
    def __init__(self, angle, size, width, color = (0,0,0)):
        self.angle = angle
        self.start_position = None
        self.end_position = None
        self.size = size
        self.width = width
        self.color = color
    
    def rotate(self):
        theta = np.radians(self.angle - 90)
        c, s = np.cos(theta), np.sin(theta)
        R = np.array(((c, -s), (s, c)))
        return R.dot(np.array([self.size,0]))

        