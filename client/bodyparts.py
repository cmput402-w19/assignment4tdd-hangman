class Body:
    def __init__(self):
        self._parts = list()

    def add_part(self, bodyPart):
        pass

    def draw(self):
        pass

    def get_part_count(self):
        pass

    def is_dead(self):
        pass

class BodyPart:
    def get_drawable(self):
        pass

class Head(BodyPart):
    pass

class Torso(BodyPart):
    pass

class LeftArm(BodyPart):
    pass

class RightArm(BodyPart):
    pass

class LeftLeg(BodyPart):
    pass

class RightLeg(BodyPart):
    pass

class Noose(BodyPart):
    pass