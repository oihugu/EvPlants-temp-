class List_of_chars(list):

    def __init__(self, *args):
        super(List_of_chars, self).__init__(args[0])

    def __getitem__(self, index):
        return super(List_of_chars, self).__getitem__(index)

    def __setitem__(self, index, value):
        super(List_of_chars, self).__setitem__(index, value)
    
    def __str__(self) -> str:
        return ''.join([str(x) for x in self])

    def __iter__(self):
        return super().__iter__()
    
    def __repr__(self) -> str:
        return super().__repr__()

    def find_all(self, elem):
        print([(a,b) for a,b in enumerate(self)])
        return [i for i, x in enumerate(self) if str(x) == str(elem)]
    
    def find(self, x):
        for index in range(self.__len__):
            if x == self.__getitem__(index):
                return index
    
    def replace(self, to_replace, replacer):
        print(f''' to_replave: {to_replace}
        replacer: {replacer}
        str: {str(self)}
        ''')
        print(self.find_all(to_replace))
        for index in self.find_all(to_replace):
            if len(replacer) == 1:
                self[index] = replacer
            else:
                del self[index]
                for a in range(len(replacer)):
                    self.insert(index + a, replacer[a])
        return self
    
