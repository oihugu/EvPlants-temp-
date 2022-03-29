from numpy import character, size


class Character():
    def __init__(self, content, default, size = None, width = None, color = None, angle_diff = None) -> None:
        self.size = size if size != None else default[0]
        self.width = width if width != None else default[1]
        self.color = color if color != None else default[2]
        self.angle_diff = angle_diff if angle_diff != None else default[3]
        self.content = content

    def __str__(self) -> str:
        return 'C(' + str(self.content) + ')'
    
    def __repr__(self) -> str:
        return 'C(' + str(self.content) + ')'
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
    
    def get_widt(self) -> float:
        return self.width
    
    def get_size(self) -> float:
        return self.size
    
    def get_content(self) -> character:
        return self.content
    
    def get_angle_diff(self) -> float:
        return self.angle_diff
    
