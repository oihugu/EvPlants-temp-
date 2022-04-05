from pyparsing import Char


class Element():
    def __init__(self, content, default, size = None, width = None, color = None, angle_diff = None) -> None:
        self.angle = default['space']['angle']
        self.size = size if size != None else default['visual']['size']
        self.width = width if width != None else default['visual']['width']
        self.color = color if color != None else default['visual']['color']
        self.angle_diff = angle_diff if angle_diff != None else default['space']['angle_diff']
        self.content = content

    def __str__(self) -> str:
        return 'C(' + str(self.content) + ')'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, other) -> bool:
        return self.content == other.content
    
    def __len__(self):
        return 0
        
    ## Setters
    def set_color(self, color) -> None:
        self.color = color
    
    def set_width(self, width) -> None:
        self.width = width
    
    def set_size(self, size) -> None:
        self.size = size
    
    def set_content(self, content) -> None:
        self.content = content
    
    def set_angle_diff(self, angle_diff) -> None:
        self.angle_diff = angle_diff

    ## Getters  
    def get_size(self) -> float:
        return self.size
    
    def get_size(self) -> float:
        return self.size
    
    def get_content(self) -> str:
        return self.content
    
    def get_angle_diff(self) -> float:
        return self.angle_diff
    
    def get_angle(self) -> float:
        return self.angle
    
    def get_color(self) -> tuple:
        return self.color
    
    def get_width(self) -> float:
        return self.width