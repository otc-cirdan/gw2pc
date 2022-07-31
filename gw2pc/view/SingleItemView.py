from django.shortcuts import render
from django.views import View
from django.utils import timezone
from gw2pc.utils import get_tradingpost_api, get_item_api
from gw2pc.view.DepthRatioTable import DepthRatioTable

class SingleItemView(View):
    depths = (1, 250, 1000, 2500, 10000)
    ratios = (('buy', 100), ('sell', 85), ('sell', 90), ('sell', 100))
    hilight_ratio = '90sell'
    hilight_depth = 2500
    include_stack = True

    def init_table(self):
        table = DepthRatioTable(api_data=self.api_data,
                                item_id=self.item_id,
                                ratios=self.ratios,
                                depths=self.depths)
        return table

    def get_api_data(self):
        self.api_data = get_tradingpost_api([self.item_id])
        self.item_data = get_item_api([self.item_id])

    def get_context_data(self, **kwargs):
        context = {}
        context['time'] = timezone.now()
        self.get_api_data()

        table = self.init_table().get_table()

        table['hilight_cols'] = [self.hilight_ratio]
        table['hilight_rows'] = [self.hilight_depth]
        table['include_stack'] = self.include_stack

        context['table'] = table

        context['hilight_depth'] = self.hilight_depth
        context['hilight_price'] = table['data']['90sell'][self.hilight_depth]
        if "item_data" in dir(self):
            context['item_name'] = self.item_data['name']
            context['item_icon'] = self.item_data['icon']

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return render(
            request,
            self.template_name,
            context,
        )