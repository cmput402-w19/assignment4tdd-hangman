from client.bodyparts import *
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

    def get_drawable(self):
        drawable = [[" " for x in range(5)] for y in range(6)]
        
        for part in self._parts:
            cordinates = part.get_cordinates()
            partDrawable = part.get_drawables()
            for i in range(len(cordinates)):
                cordinate = cordinates[i]
                symbol = partDrawable[i]
                drawable[cordinate[1]][cordinate[0]] = symbol
        drawableString = ""
        for y in range(len(drawable)):
            row = drawable[y]
            for col in row:
                drawableString += col
            if y != len(drawable) - 1:
                drawableString += "\n"
        return drawableString

    def get_part_count(self):
        return len(self._parts)

    def is_dead(self):
        return self.get_part_count() == 7