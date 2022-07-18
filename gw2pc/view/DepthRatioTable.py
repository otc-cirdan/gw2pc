class DepthRatioTable():
    def __init__(self, api_data=None, item_id=None, ratios=None, depths=None, *args, **kwargs):
        self.api_data = api_data
        self.item_id = item_id
        self.ratios = ratios
        self.depths = depths

    def get_price(self, buysell, depth, percent):
        price = self.api_data[self.item_id].get_price(depth, buysell)
        if price is None:
            return 0
        return price * (percent / 100)

    def get_table(self):
        data = {}
        for buysell, percent in self.ratios:
            # Fill in the rest of the column with the deepest depth price if there is no available data for greater depths
            # get highest depth price, assuming self.depths goes from smallest to biggest depth
            highest_depth_price = 0
            # Initialize empty table cell
            data[f'{percent}{buysell}'] = {}
            for depth in self.depths:
                # Update cell with price
                data[f'{percent}{buysell}'][depth] = self.get_price(buysell, depth, percent)
                
                if data[f'{percent}{buysell}'][depth] != 0:
                    highest_depth_price = data[f'{percent}{buysell}'][depth]
                else:
                    # Fill zero listing cells with deepest depth price we've found
                    data[f'{percent}{buysell}'][depth] = highest_depth_price
                

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
            'data': data,
        }
        return table