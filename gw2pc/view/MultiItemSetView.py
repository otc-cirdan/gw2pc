from gw2pc.utils import get_tradingpost_api
from gw2pc.view.SingleItemView import SingleItemView
from gw2pc.view.MultiItemSetDepthRatioTable import MultiItemSetDepthRatioTable
from gw2pc.view.MultiItemSetItemDepthTable import MultiItemSetItemDepthTable

class MultiItemSetView(SingleItemView):
    include_stack = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.items = {k:v for k,v in self.items_tuples}
        self.item_ids = self.items.values()

    def get_api_data(self):
        self.api_data = get_tradingpost_api(self.item_ids)

    def init_table(self):
        table = MultiItemSetDepthRatioTable(api_data=self.api_data,
                                            item_ids=self.item_ids,
                                            ratios=self.ratios,
                                            depths=self.depths)
        return table

    def init_item_table(self):
        item_table = MultiItemSetItemDepthTable(items_tuples=self.items_tuples,
                                                   api_data=self.api_data,
                                                   ratios=self.ratios,
                                                   depths=self.depths)
        return item_table

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        item_table = self.init_item_table().get_table()
        item_table['hilight_cols'] = [self.hilight_depth]
        context['item_table'] = item_table

        return context