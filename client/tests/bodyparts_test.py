import unittest
from client.bodyparts import *

class BodyPartTestCase(unittest.TestCase):
    def setUp(self):
        self.stickFigure = (
                       (" ", " ", "|", " ", " "),
                       (" ", " ", "|", " ", " "),
                       ("(", "o", "_", "O", ")"),
                       (" ", "/", "|", "\\", " "),
                       (" ", " ", "|", " ", " "),
                       (" ", "/", " ", "\\", " ")
            )

    def tearDown(self):
        self.stickFigure = None

    def test_parts_drawable(self):
        parts = [Noose(), Head(), Torso(), LeftArm(), RightArm(), LeftLeg(), RightLeg()]
        
        for i in range(len(parts)):
            cordinates = parts[i].get_cordinates()
            drawables = parts[i].get_drawables()
            for j in len(cordinates):
                cordinate = [j]
                drawable= drawables[j]
                self.assertEqual(self.stickFigure[cordinate[1]][cordinate[0]], drawable)

if __name__ == '__main__':
    unittest.main()