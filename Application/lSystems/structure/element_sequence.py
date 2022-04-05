class Element_sequence():

    def __init__(self):
        self.ls = []
    
        
    def __getitem__(self, index):
        return self.ls[index]

    def __setitem__(self, index, value):
        self.ls[index] = value
    
    def __len__(self):
        return len(self.ls)
    
    def __str__(self) -> str:
        s = 'E[' 
        for i, x in enumerate(self.ls):
            if i != len(self.ls) - 1:
                s += str(x) + ', '
            else:
                s += str(x)
        s += ']'
        return s

    def __repr__(self) -> str:
        return self.__str__()

    def __delitem__(self, idx):
        del self.ls[idx]
 
    def find_all(self, elem):
        return [i for i, x in enumerate(self.ls) if str(x) == str(elem)]
    
    def find(self, x):
        for index in range(len(self.ls)):
            if x == self.ls[index]:
                return index
               
    def append(self, x):
        self.ls.append(x)
    
    def insert(self, index, x):
        self.ls[index] = x
        
    def insert_element_sequence(self, index, element_sequence):
        if len(element_sequence) == 0:
            self.insert(index, element_sequence)
        else:
            temp_start = self.ls[:index]
            for i in range(len(element_sequence)):
                temp_start.append(element_sequence[i])
            self.ls = temp_start + self.ls[index+1:]

    def replace(self, to_replace, replacer):
        for index in self.find_all(to_replace):
            self.insert_element_sequence(index, replacer)
        

