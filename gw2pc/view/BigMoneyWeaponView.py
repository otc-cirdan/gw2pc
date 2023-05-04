from django.shortcuts import render
from django.views import View
from django.utils import timezone
from gw2pc.utils import get_tradingpost_api

class BigMoneyWeaponView(View):
    template_name = 'gw2pc/legendaries.html'
    template_description = ""
    item_tuples = []
    sell_table_percentage = 85

    def init_table(self):
        leg_items = {k:v for k,v in self.item_tuples}
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
                price = api_data[item].get_sell_price(depth)
                if price is not None:
                    price = price * (self.sell_table_percentage / 100)
                leg_sell_data[item][depth] = {'val': price}
                if price and not sell_hilight_lock and depth != leg_sell_hilight and depth <= sell_hilight_max:
                    if leg_sell_data[item][depth]['val'] - leg_sell_data[item][leg_sell_hilight]['val'] > sell_hilight_thresh:
                        leg_sell_hilight = depth
                    else:
                        sell_hilight_lock = True
                leg_buy_data[item][depth] = api_data[item].get_buy_price(depth)
            if leg_sell_data[item][leg_sell_hilight]['val'] is not None and leg_sell_data[item][leg_sell_hilight]['val'] > 0:
                leg_sell_data[item][leg_sell_hilight]['hilight'] = True

        leg_sell_table = {
            'r1c1': {
                'content': 'Item',
            },
            'columns': [{'key': x, 'content': f'Depth {x}'} for x in (leg_item_depths)],
            'rows': [{'content': e1, 'key': e2} for e1,e2 in self.item_tuples],
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
            'rows': [{'content': e1, 'key': e2} for e1,e2 in self.item_tuples],
            'data': leg_buy_data,
            'row_first': True,
            'row_link': 'gw2bltc',
            'format': 'gs',
        }
        return leg_buy_table, leg_sell_table

    def get_context_data(self, **kwargs):
        context = {}
        context['time'] = timezone.now()

        leg_buy_table, leg_sell_table = self.init_table()

        context['leg_sell_table'] = leg_sell_table
        context['leg_buy_table'] = leg_buy_table
        
        context['template_description'] = self.template_description
        context['sell_table_percentage'] = self.sell_table_percentage
        context['url_path'] = self.request.path

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return render(
            request,
            self.template_name,
            context,
        )