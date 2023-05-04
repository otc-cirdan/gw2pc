from django.shortcuts import render
from gw2pc.view.BaseItemView import BaseItemView
from django.utils import timezone
from gw2pc.utils import get_tradingpost_api, get_item_api
from gw2pc.view.DepthRatioTable import DepthRatioTable

class SingleItemView(BaseItemView):
    template_name = 'gw2pc/singleitem.html'

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
        context = super().get_context_data(**kwargs)

        context['item_id'] = self.item_id

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return render(
            request,
            self.template_name,
            context,
        )