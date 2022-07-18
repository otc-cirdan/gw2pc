from gw2pc.view.SingleItemView import SingleItemView

# Uses the singleitem.html template to render prices for a single gw2 item
# Must include properties:
# item_id => GW2 Item's ID, ex: 30689
# item_name => GW2 Item's Name, ex: Eternity
# url_path => short url path used to host the single item's page, will be concatenated like: "https://gw2pc.com/{ url_path }/"
class ManagedSingleItemView(SingleItemView):
    template_name = 'gw2pc/singleitem.html'
    depths = (1, 500, 1000, 2000, 3000, 4000, 5000)
    hilight_depth = 2000

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_id'] = self.item_id
        context['url_path'] = self.url_path
        return context