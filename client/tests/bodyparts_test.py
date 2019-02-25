import unittest
from client.bodyparts import *

class BodyPartTestCase(unittest.TestCase):
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

    def test_parts_drawable(self):
        parts = [Noose(), Head(), Torso(), LeftArm(), RightArm(), LeftLeg(), RightLeg()]
        drawables = ["|\n|", "[o_o]", "|", "\\", "/", "_/", "\\_"]
        for i in range(len(parts)):
            self.assertIs(parts[i], drawables[i])

if __name__ == '__main__':
    unittest.main()