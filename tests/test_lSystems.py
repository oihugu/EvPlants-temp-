from  Application.lSystems import L_system
import unittest

class TestLSystems(unittest.TestCase):
    
    def test_lSystems(self):
        assert(L_system('F', {'F': 'F+F-F-F+F'}) == L_system('F', {'F': 'F+F-F-F+F'}))
        

if __name__ == "__main__":
    unittest.main()