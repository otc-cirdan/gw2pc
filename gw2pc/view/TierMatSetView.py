from gw2pc.view.MultiItemSetView import MultiItemSetView

class TierMatSetView(MultiItemSetView):
    hilight_depth = 250
    depths = (1, 100, 250, 1000, 5000)
    template_name = 'gw2pc/t6.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mat_tier'] = self.mat_tier
        return context