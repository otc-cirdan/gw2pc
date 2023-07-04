from django.views import View
from django.utils import timezone
from django.shortcuts import render
from gw2pc.utils import get_tradingpost_api
from gw2pc.view.CraftedGiftDepthRatioTable import CraftedGiftDepthRatioTable

class CraftedGiftItemView(View):
    template_name = 'gw2pc/condensedgift.html'
    depths = (250, 2000, 5000)
    hilight_depth = 2000
    include_stack = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.items = {k:v for k,v in self.items_tuples}
        self.item_ids = []
        self.item_components = {}
        for item, item_recipe in self.items.items():
            if type(item_recipe[0]) is tuple:
                # Lower order item, add each item_id in item_recipe to item_ids
                for component in item_recipe:
                    self.item_ids.append(component[0])
            elif type(item_recipe[0]) is str:
                # Higher order item, set ingredient list
                self.item_components[item] = item_recipe

    def get_api_data(self):
        self.api_data = get_tradingpost_api(self.item_ids)

    def init_table(self):
        table = CraftedGiftDepthRatioTable(api_data=self.api_data,
                                           items=self.items,
                                           item_components=self.item_components,
                                           depths=self.depths)
        return table

    def get_context_data(self, **kwargs):
        context = {}
        context['time'] = timezone.now()
        context['url_path'] = self.request.path

        self.get_api_data()

        table = self.init_table().get_table()

        table['hilight_cols'] = [self.hilight_depth]
        table['include_stack'] = self.include_stack

        context['table'] = table
        context['hilight_depth'] = self.hilight_depth

        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return render(
            request,
            self.template_name,
            context,
        )