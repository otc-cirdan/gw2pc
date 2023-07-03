from gw2pc.view.DepthRatioTable import DepthRatioTable

class CraftedGiftDepthRatioTable(DepthRatioTable):
    def __init__(self, items, item_components, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.items = items
        self.item_components = item_components

    def get_table(self):
        data = {}
        for item_name, recipe in self.items.items():
            key = "_".join(item_name.split(" "))
            data[key] = {}
            for depth in self.depths:
                sell_price = 0
                for entry in recipe:
                    if type(entry) is tuple:
                        item_id, quantity = entry
                        sell_price += self.api_data[item_id].get_sell_price(depth) * quantity
                    elif type(entry) is str:
                        # Will have to compute the component values AFTER this loop if you wish to
                        # reorder the higher order items to somewhere other than the bottom of the table
                        # after all the ingredients have been price checked and put into data
                        component_name = "_".join(entry.split(" "))
                        sell_price += data[component_name][depth]
                data[key][depth] = sell_price

        table = {
            'r1c1': {
                'content': 'Item',
            },
            'columns': [{'key': x, 'content': f'Depth {x}'} for x in (self.depths)],
            'rows': [ {'content': item_name, 'key': "_".join(item_name.split(" "))} for item_name in self.items.keys() ],
            'data': data,
            'row_first': True,
            'row_link': 'gw2wiki',
        }
        return table