class Body:
    def __init__(self):
        self._parts = list()

    def add_part(self, bodyPart):
        if not isinstance(bodyPart, BodyPart):
            return
        for part in self._parts:
            if isinstance(bodyPart, type(part)):
                return
        self._parts.append(bodyPart)

    def draw(self):
        pass

    def get_part_count(self):
        return len(self._parts)

    def is_dead(self):
        return self.get_part_count() == 7

class BodyPart:
    def get_drawable(self):
        pass

class Head(BodyPart):
    def get_drawable(self):
        return "[o_o]"

class Torso(BodyPart):
    def get_drawable(self):
        return "|"

class LeftArm(BodyPart):
    def get_drawable(self):
        return "\\"

class RightArm(BodyPart):
    def get_drawable(self):
        return "/"

class LeftLeg(BodyPart):
    def get_drawable(self):
        return "_/"

class RightLeg(BodyPart):
    def get_drawable(self):
        return "\\_"

class Noose(BodyPart):
    def get_drawable(self):
        return "|\n|"