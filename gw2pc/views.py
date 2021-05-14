from django.shortcuts import render
from django.utils import timezone
from django.views import View
from gw2pc.utils import get_tradingpost_api


def gw2pc_t6(request):
    # T6 set.
    context = {}
    context['time'] = timezone.now()

    t6_items_tuples = (
        ('Blood',  24295),
        ('Bones',  24358),
        ('Claws',  24351),
        ('Dust',   24277),
        ('Fangs',  24357),
        ('Scales', 24289),
        ('Totems', 24300),
        ('Venom',  24283),
    )
    t6_items = {k:v for k,v in t6_items_tuples}
    context['t6_items_tuples'] = t6_items_tuples
    api_data = get_tradingpost_api(t6_items.values())

    t6_item_data = {}
    t6_item_depths = (1, 100, 250, 1000, 5000)
    max_item_depth = 5000
    for item in t6_items.values():
        t6_item_data[item] = {}
        for depth in t6_item_depths:
            t6_item_data[item][depth] = api_data[item].get_sell_price(depth)
    t6_item_table = {
        'r1c1': {
            'content': 'Item',
        },
        'columns': [{'key': x, 'content': f'Depth {x}'} for x in (t6_item_depths) if x <= max_item_depth],
        'rows': [{'content': e1, 'key': e2} for e1,e2 in t6_items_tuples],
        'hilight_cols': [250],
        'data': t6_item_data,
        'row_first': True,
        'row_link': 'gw2bltc',
    }
    context['t6_item_table'] = t6_item_table

    t6_set_data = {}
    for buysell, percent in (('buy', 100), ('sell', 85), ('sell', 90), ('sell', 100)):
        t6_set_data[f'{percent}{buysell}'] = {}
        for depth in t6_item_depths:
            price = 0
            for item in t6_items.values():
                if buysell == 'buy':
                    itemprice = api_data[item].get_buy_price(depth)
                else:
                    itemprice = api_data[item].get_sell_price(depth)
                price += itemprice * (percent / 100) * 250
            t6_set_data[f'{percent}{buysell}'][depth] = price
    t6_set_table = {
        'r1c1': {
            'content': 'Depth',
        },
        'columns': [
            { 'key': '100buy', 'content': '100% Buy', },
            { 'key': '85sell', 'content': '85% Sell', },
            { 'key': '90sell', 'content': '90% Sell', },
            { 'key': '100sell', 'content': '100% Sell', },
        ],
        'rows': [{'content': x, 'key': x} for x in t6_item_depths],
        'hilight_cols': ['90sell'],
        'hilight_rows': [250],
        'data': t6_set_data,
    }


    context['t6_set_table'] = t6_set_table
    context['t6_set_data'] = t6_set_data
    context['t6_set_types'] = ('100buy', '85sell', '90sell', '100sell')

    return render(
        request,
        'gw2pc/t6.html',
        context,
    )


class SingleItemView(View):
    depths = (1, 250, 1000, 2500, 10000)
    ratios = (('buy', 100), ('sell', 85), ('sell', 90), ('sell', 100))
    hilight_ratio = '90sell'
    hilight_depth = 2500
    include_stack = True

    def get(self, request, *args, **kwargs):
        context = {}
        context['time'] = timezone.now()

        api_data = get_tradingpost_api([self.item_id])

        data = {}
        for buysell, percent in self.ratios:
            data[f'{percent}{buysell}'] = {}
            for depth in self.depths:
                if buysell == 'buy':
                    price = api_data[self.item_id].get_buy_price(depth)
                else:
                    price = api_data[self.item_id].get_sell_price(depth)
                data[f'{percent}{buysell}'][depth] = price * (percent / 100)
        table = {
            'r1c1': {
                'content': 'Depth',
            },
            'columns': [
                {'key': f"{percent}{buysell}",
                 'content': f"{percent}% {buysell.title()}"}
                for buysell, percent in self.ratios
            ],
            'rows': [{'content': x, 'key': x} for x in self.depths],
            'hilight_cols': [self.hilight_ratio],
            'hilight_rows': [self.hilight_depth],
            'data': data,
            'include_stack': self.include_stack,
        }

        context['table'] = table

        return render(
            request,
            self.template_name,
            context,
        )


class MCView(SingleItemView):
    item_id = 19976
    template_name = 'gw2pc/mc.html'
    hilight_ratio = '100buy'


class EctoView(SingleItemView):
    item_id = 19721
    template_name = 'gw2pc/ecto.html'
    depths = (1, 500, 1000, 2000, 3000, 4000, 5000)
    hilight_depth = 2000


def gw2pc_leg(request):
    # Legendary Weapons.
    context = {}
    context['time'] = timezone.now()

    leg_items_tuples = (
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
    )
    leg_items = {k:v for k,v in leg_items_tuples}
    context['leg_items_tuples'] = leg_items_tuples
    api_data = get_tradingpost_api(leg_items.values())

    leg_sell_data = {}
    leg_buy_data = {}
    leg_item_depths = (1, 2, 3, 5)
    for item in leg_items.values():
        leg_sell_data[item] = {}
        leg_buy_data[item] = {}
        leg_sell_hilight = leg_item_depths[0]
        sell_hilight_lock = False
        sell_hilight_thresh = 450000
        sell_hilight_max = 3
        for depth in leg_item_depths:
            leg_sell_data[item][depth] = {'val': api_data[item].get_sell_price(depth) * (85 / 100)}
            if not sell_hilight_lock and depth != leg_sell_hilight and depth <= sell_hilight_max:
                if leg_sell_data[item][depth]['val'] - leg_sell_data[item][leg_sell_hilight]['val'] > sell_hilight_thresh:
                    leg_sell_hilight = depth
                else:
                    sell_hilight_lock = True
            leg_buy_data[item][depth] = api_data[item].get_buy_price(depth)
        leg_sell_data[item][leg_sell_hilight]['hilight'] = True

    leg_sell_table = {
        'r1c1': {
            'content': 'Item',
        },
        'columns': [{'key': x, 'content': f'Depth {x}'} for x in (leg_item_depths)],
        'rows': [{'content': e1, 'key': e2} for e1,e2 in leg_items_tuples],
        'data': leg_sell_data,
        'row_first': True,
        'row_link': 'gw2bltc',
        'format': 'gs',
    }
    leg_buy_table = {
        'r1c1': {
            'content': 'Item',
        },
        'columns': [{'key': x, 'content': f'Depth {x}'} for x in (leg_item_depths)],
        'rows': [{'content': e1, 'key': e2} for e1,e2 in leg_items_tuples],
        'data': leg_buy_data,
        'row_first': True,
        'row_link': 'gw2bltc',
        'format': 'gs',
    }
    context['leg_sell_table'] = leg_sell_table
    context['leg_buy_table'] = leg_buy_table

    return render(
        request,
        'gw2pc/legendaries.html',
        context,
    )
