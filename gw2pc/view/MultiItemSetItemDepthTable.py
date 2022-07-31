from gw2pc.view.DepthRatioTable import DepthRatioTable

class MultiItemSetItemDepthTable(DepthRatioTable):
    def __init__(self, items_tuples=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.items_tuples = items_tuples
        self.item_ids = [x[1] for x in items_tuples]

    def get_table(self):
        data = {}
        for item in self.item_ids:
            data[item] = {}
            for depth in self.depths:
                data[item][depth] = self.api_data[item].get_sell_price(depth)
        table = {
            'r1c1': {
                'content': 'Item',
            },
            'columns': [{'key': x, 'content': f'Depth {x}'} for x in (self.depths)],
            'rows': [{'content': e1, 'key': e2} for e1,e2 in self.items_tuples],
            'data': data,
            'row_first': True,
            'row_link': 'gw2bltc',
        }
        return table