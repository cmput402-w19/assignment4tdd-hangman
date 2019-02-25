class BodyPart:
    def get_cordinates(self):
        pass
    def get_drawables(self):
        pass

class Head(BodyPart):
    def get_cordinates(self):
        return ((0, 2), (1, 2), (2, 2), (3, 2), (4, 2))
    def get_drawables(self):
        return "(o_O)"

class Torso(BodyPart):
    def get_cordinates(self):
        return ((2, 3), (2, 4))
    def get_drawables(self):
        return "||"

class LeftArm(BodyPart):
    def get_cordinates(self):
        return ((1, 3),)
    def get_drawables(self):
        return "/"

class RightArm(BodyPart):
    def get_cordinates(self):
        return ((3, 3),)
    def get_drawables(self):
        return "\\"

class LeftLeg(BodyPart):
    def get_cordinates(self):
        return ((0, 5), (1, 5))
    def get_drawables(self):
        return "_/"

class RightLeg(BodyPart):
    def get_cordinates(self):
        return ((3, 5), (4, 5))
    def get_drawables(self):
        return "\\_"

class Noose(BodyPart):
    def get_cordinates(self):
        return ((2, 0), (2, 1))
    def get_drawables(self):
        return "||"