class Element_sequence(list):

    def __init__(self, *args):
        super(Element_sequence, self).__init__(args[0])

    def __getitem__(self, index):
        return super(Element_sequence, self).__getitem__(index)

    def __setitem__(self, index, value):
        super(Element_sequence, self).__setitem__(index, value)
    
    def __str__(self) -> str:
        return ''.join([str(x) for x in self])

    def __iter__(self):
        return super().__iter__()
    
    def __repr__(self) -> str:
        return super().__repr__()

    def find_all(self, elem):
        return [i for i, x in enumerate(self) if str(x) == str(elem)]
    
    def find(self, x):
        for index in range(self.__len__):
            if x == self.__getitem__(index):
                return index
    
    def insert_element_sequence(self, index, element_sequence):
        for i in range(len(element_sequence)):
            self.insert(index + i, element_sequence[i])

    def replace(self, to_replace, replacer):
        for index in self.find_all(to_replace):
            if len(replacer) == 1:
                self[index] = replacer[0]
            else:
                del self[index]
                self.insert_element_sequence(index, replacer)
        return self
    

