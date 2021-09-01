from mob_class import Mob


class NPC(Mob):
    def __init__(self, name, hp, ac, stren, dex, con, wis, intel, chari):
        super().__init__(name=name, hp=hp, ac=ac, stren=stren, dex=dex, con=con, wis=wis, intel=intel, chari=chari)