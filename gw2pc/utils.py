import requests


class ItemInfo(object):
    def __init__(self, iteminfo):
        self.item_id = iteminfo['id']
        self.buys = iteminfo['buys']
        self.sells = iteminfo['sells']

    def get_buy_price(self, depth=1):
        return self._get_price(self.buys, depth=depth)

    def get_sell_price(self, depth=1):
        return self._get_price(self.sells, depth=depth)

    def _get_price(self, data, depth):
        current_price = None
        items_seen = 0
        for listing in data:
            current_price = listing['unit_price']
            items_seen += listing['quantity']
            if items_seen >= depth:
                return current_price


def get_tradingpost_api(item_ids):
    r = requests.get('https://api.guildwars2.com/v2/commerce/listings?ids=' + ','.join([str(x) for x in item_ids]))
    r.raise_for_status()
    data = r.json()
    res = {}
    if isinstance(data, dict):
        # If we got a dictionary, then there's only one item id. Let's just make it an array
        # so we only have to write the rest of this function once.
        data = [data]

    for iteminfo in data:
        res[iteminfo['id']] = ItemInfo(iteminfo)
        # Well, that was easy

    return res




