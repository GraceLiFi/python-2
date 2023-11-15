from src.student.Character import Character


class Dwarf(Character):
    def __repr__(self):
        return f"Drawf: {self.hit_points} hit points."