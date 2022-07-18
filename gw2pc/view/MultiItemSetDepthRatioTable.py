from gw2pc.view.DepthRatioTable import DepthRatioTable

class MultiItemSetDepthRatioTable(DepthRatioTable):
    def __init__(self, item_ids=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.item_ids = item_ids

    def get_price(self, buysell, depth, percent):
        price = 0
        for item_id in self.item_ids:
            itemprice = self.api_data[item_id].get_price(depth, buysell)
            price += itemprice * (percent / 100) * 250
        return price