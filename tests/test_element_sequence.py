from  Application.lSystems.structure import Element_sequence
import unittest

class TestElementSequence(unittest.TestCase):
    
    def __init__(self):
        self.es = Element_sequence()
        self.es.append(1)
        self.es.append(1)
        self.es.append(2)
        self.es.append(3)
        self.es.append(2)
        self.es.append(1)
        self.es.append(2)
        
    def testES_getitem(self):
        assert self.es[0] == 1
        assert self.es[1] == 1
        assert self.es[2] == 2
        assert self.es[-1] == 2
    
    def testES_find_all(self):
        assert self.es.find_all(1) == [0, 1, 5]
    
    def testES_str(self):
        assert str(self.es) == '[1, 1, 2, 3, 2, 1, 2]'

if __name__ == "__main__":
    unittest.main()