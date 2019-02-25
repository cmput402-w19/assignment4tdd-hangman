import unittest
from client.body import *
from client.bodyparts import *

class BodyTestCase(unittest.TestCase):
    def setUp(self):
        self.body = Body()

    def tearDown(self):
        self.body = None

    def test_empty_body(self):
        self.assertIs(self.body.is_dead(), False)
    
    def test_full_body(self):
        self.body.add_part(Noose())
        self.body.add_part(Head())
        self.body.add_part(Torso())
        self.body.add_part(LeftArm())
        self.body.add_part(RightArm())
        self.body.add_part(LeftLeg())
        self.body.add_part(RightLeg())
        self.assertIs(self.body.is_dead(), True)

    def test_duplicate_body_parts(self):
        self.body.add_part(Noose())
        self.body.add_part(Head())
        self.body.add_part(Torso())
        self.body.add_part(LeftLeg())
        self.body.add_part(LeftLeg())
        self.body.add_part(LeftLeg())
        self.body.add_part(LeftLeg())
        self.assertIs(self.body.is_dead(), False)

    def test_invalid_body_parts(self):
        self.body.add_part(Noose())
        self.body.add_part(Head())
        self.body.add_part(Torso())
        self.body.add_part(1)
        self.body.add_part(2)
        self.body.add_part("--")
        self.body.add_part("ABC")
        self.assertIs(self.body.is_dead(), False)

    def test_body_count(self):
        self.body.add_part(Noose())
        self.assertIs(self.body.get_part_count(), 1)
        self.body.add_part(Head())
        self.assertIs(self.body.get_part_count(), 2)
        self.body.add_part(Torso())
        self.assertIs(self.body.get_part_count(), 3)
        self.body.add_part(LeftArm())
        self.assertIs(self.body.get_part_count(), 4)
        self.body.add_part(RightArm())
        self.assertIs(self.body.get_part_count(), 5)
        self.body.add_part(LeftLeg())
        self.assertIs(self.body.get_part_count(), 6)
        self.body.add_part(RightLeg())
        self.assertIs(self.body.get_part_count(), 7)

    def test_duplicate_body_count(self):
        self.body.add_part(Noose())
        self.assertIs(self.body.get_part_count(), 1)
        self.body.add_part(Head())
        self.assertIs(self.body.get_part_count(), 2)
        self.body.add_part(Head())
        self.assertIs(self.body.get_part_count(), 2)
        self.body.add_part(Noose())
        self.assertIs(self.body.get_part_count(), 2)
        self.body.add_part(RightArm())
        self.assertIs(self.body.get_part_count(), 3)

    def test_invalid_body_count(self):
        self.body.add_part(Noose())
        self.assertIs(self.body.get_part_count(), 1)
        self.body.add_part(Head())
        self.assertIs(self.body.get_part_count(), 2)
        self.body.add_part(1)
        self.assertIs(self.body.get_part_count(), 2)
        self.body.add_part("LEG")
        self.assertIs(self.body.get_part_count(), 2)
        self.body.add_part(RightArm())
        self.assertIs(self.body.get_part_count(), 3)

    def test_empty_body_drawable(self):
        lines = self.body.get_drawable().split("\n")
        self.assertIs(len(drawable), 6)
        for line in lines:
            self.assertIs(len(drawable), 5)

    def test_body_drawable(self):
        head = Head()
        head.get_drawables = unittest.mock.Mock()
        head.get_drawables.return_value = ("123")
        head.get_cordinates = unittest.mock.Mock()
        head.get_cordinates.return_value = ((0, 1), (0, 2), (3, 3))

        self.body.add_part(head)
        lines = self.body.get_drawable().split("\n")
        self.assertEqual(lines[1][0], "1")
        self.assertEqual(lines[2][0], "2")
        self.assertEqual(lines[3][3], "3")
if __name__ == '__main__':
    unittest.main()