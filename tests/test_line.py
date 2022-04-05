import unittest
from ..lSystems.structure import Linha

class TestLines(unittest.TestCase):

    def test_lines(self):
        l = Linha(angle=90, size=1, width=1, color=(0,0,0))

        assert l.angle == 90
        assert l.size == 1
        assert l.width == 1
        assert l.color == (0,0,0)

        l.start_position = (0,0)
        l.end_position = (0,1)

        assert l.start_position == (0,0)
        assert l.end_position == (0,1)

        assert l.rotate() == (1,0)




if __name__ == "__main__":
    unittest.main()