import enum

class BaseEnum(enum.Enum):
    @classmethod
    def values_list(cls):
        return list(map(lambda c: c.value, cls))


class UniteItems(BaseEnum):
    MUSCLE_BAND = "Muscle Band"
    SCOPE_LENS = 'Scope Lens'
    SHELL_BELL = 'Shell Bell'
    WISE_GLASSES = 'Wise Glasses'
    FOCUS_BAND = 'Focus Band'
    ENERGY_AMPLIFIER = 'Energy Amplifier'
    FLOAT_STONE = 'Float Stone'
    BUDDY_BARRIER = 'Buddy Barrier'
    SCORE_SHIELD = 'Score Shield'
    AEOS_COOKIE = 'Aeos Cookie'
    ATTACK_WEIGHT = 'Attack Weight'
    SP_ATK_SPECS = 'Sp Atk Specs'
    LEFTOVERS = 'Leftovers'
    ASSAULT_VEST = 'Assault Vest'
    ROCKY_HELMET = 'Rocky Helmet'


class UniteInformation(BaseEnum):
    LEVELS = 'Levels'
    ITEM_ENHANCERS = 'Item Enhancers'
    ITEM_ENHANCERS_PER_LEVEL = 'Item Enhancers / Level'
    DOLLARS = 'Dollars'
    DOLLARS_PER_LEVEL = 'Dollars / Level'
    