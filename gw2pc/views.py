from gw2pc.view.SingleItemView import SingleItemView
from gw2pc.view.TierMatSetView import TierMatSetView
from gw2pc.view.BigMoneyWeaponView import BigMoneyWeaponView


class MCView(SingleItemView):
    item_id = 19976
    template_name = 'gw2pc/mc.html'
    hilight_ratio = '100buy'

class EctoView(SingleItemView):
    item_id = 19721
    template_name = 'gw2pc/ecto.html'
    depths = (1, 500, 1000, 2000, 3000, 4000, 5000)
    hilight_depth = 2000

class StabMatrixView(SingleItemView):
    item_id = 73248
    depths = (1, 250, 500, 1000, 5000, 10000, 20000)
    hilight_depth = 1000

class FractalEncryptionView(SingleItemView):
    item_id = 75919
    depths = (1, 250, 500, 1000, 5000, 10000, 20000)
    hilight_depth = 1000

class AssView(SingleItemView):
    item_id = 96978
    depths = (1, 50, 100, 250, 500, 1000)
    hilight_depth = 250

class AmbergrisView(SingleItemView):
    item_id = 96347

class PureJadeView(SingleItemView):
    item_id = 97102

class RunestoneView(SingleItemView):
    item_id = 96722

class AureneMemoryView(SingleItemView):
    item_id = 96088

class MemoryOfBattleView(SingleItemView):
    item_id = 71581

class ShardOfGloryView(SingleItemView):
    item_id = 70820
    depths = (1, 250, 1000, 5000, 10000, 50000, 100000)
    hilight_depth = 5000

class LamplighterBadgeView(SingleItemView):
    item_id = 97790
    depths = (1, 50, 100, 250, 500)
    hilight_depth = 250

class AmalgamatedGemstoneView(SingleItemView):
    item_id = 68063

class T3SetView(TierMatSetView):
    items_tuples = (
        ('Blood',  24292),
        ('Bones',  24344),
        ('Claws',  24348),
        ('Dust',   24274),
        ('Fangs',  24354),
        ('Scales', 24286),
        ('Totems', 24298),
        ('Venom',  24280),
    )
    mat_tier = 3


class T4SetView(TierMatSetView):
    items_tuples = (
        ('Blood',  24293),
        ('Bones',  24345),
        ('Claws',  24349),
        ('Dust',   24275),
        ('Fangs',  24355),
        ('Scales', 24287),
        ('Totems', 24363),
        ('Venom',  24281),
    )
    mat_tier = 4
    
class T5SetView(TierMatSetView):
    items_tuples = (
        ('Blood',  24294),
        ('Bones',  24341),
        ('Claws',  24350),
        ('Dust',   24276),
        ('Fangs',  24356),
        ('Scales', 24288),
        ('Totems', 24299),
        ('Venom',  24282),
    )
    mat_tier = 5


class T6SetView(TierMatSetView):
    items_tuples = (
        ('Blood',  24295),
        ('Bones',  24358),
        ('Claws',  24351),
        ('Dust',   24277),
        ('Fangs',  24357),
        ('Scales', 24289),
        ('Totems', 24300),
        ('Venom',  24283),
    )
    mat_tier = 6

class PrecursorWeaponView(BigMoneyWeaponView):
    template_description = "Precursor Weapon"
    sell_table_percentage = 90
    item_tuples = (
        ('Dawn',  29169),
        ('Dusk',  29185),
        ('Zap',  29181),
        ('The Legend',  29180),
        ('Storm',  29176),
        ('The Chosen',  29177),
        ('The Lover',  29178),
        ('Tooth of Frostfang',  29166),
        ('Leaf of Kudzu',  29172),
        ('Spark',  29167),
        ('Howl',  29184),
        ('The Bard',  29168),
        ('The Hunter',  29175),
        ('Rodgort\'s Flame',  29182),
        ('The Colossus',  29170),
        ('The Energizer',  29173),
        ('Chaos Gun',  29174),
        ('Venom',  29183),
        ('Rage',  29179),
        ('Carcharias',  29171),
        ('Dragon\'s Rending',  97449),
        ('Dragon\'s Claw',  95967),
        ('Dragon\'s Tail',  96827),
        ('Dragon\'s Argument',  96915),
        ('Dragon\'s Wisdom',  96193),
        ('Dragon\'s Fang',  95994),
        ('Dragon\'s Gaze',  96303),
        ('Dragon\'s Scale',  97691),
        ('Dragon\'s Breath',  96925),
        ('Dragon\'s Voice',  97513),
        ('Dragon\'s Bite',  96357),
        ('Dragon\'s Weight',  95920),
        ('Dragon\'s Flight',  95834),
        ('Dragon\'s Persuasion',  97267),
        ('Dragon\'s Wing',  96330),
        ('Dragon\'s Insight',  95814),
    )

class LegendaryWeaponView(BigMoneyWeaponView):
    template_description = "Legendary Weapon"
    # sell_table_percentage = 85 # default
    item_tuples = (
        ('Eternity',  30689),
        ('Sunrise',  30703),
        ('Twilight',  30704),
        ('Bolt',   30699),
        ('The Bifrost',  30698),
        ('Meteorlogicus',  30695),
        ('The Flameseeker Prophecies',  30696),
        ('The Dreamer', 30686),
        ('Frostfang', 30684),
        ('Kudzu',  30685),
        ('Incinerator',  30687),
        ('Howler',  30702),
        ('Minstrel',  30688),
        ('The Predator',  30694),
        ('Rodgort',  30700),
        ('The Juggernaut',  30690),
        ('The Moot',  30692),
        ('Quip',  30693),
        ('Kraitkin',  30701),
        ('Frenzy',  30697),
        ('Kamohoali\'i Kotaki',  30691),
        ('Aurene\'s Rending',  96937),
        ('Aurene\'s Claw',  96203),
        ('Aurene\'s Tail',  95612),
        ('Aurene\'s Argument',  95808),
        ('Aurene\'s Wisdom',  96221),
        ('Aurene\'s Fang',  95675),
        ('Aurene\'s Gaze',  97165),
        ('Aurene\'s Scale',  96028),
        ('Aurene\'s Breath',  97099),
        ('Aurene\'s Voice',  97783),
        ('Aurene\'s Bite',  96356),
        ('Aurene\'s Weight',  95684),
        ('Aurene\'s Flight',  97590),
        ('Aurene\'s Persuasion',  97377),
        ('Aurene\'s Wing',  97077),
        ('Aurene\'s Insight',  96652),
    )