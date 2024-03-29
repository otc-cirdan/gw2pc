from django.shortcuts import render
from django.views import View
from django.utils import timezone

class BaseItemView(View):
    depths = (1, 500, 1000, 2000, 3000, 4000, 5000)
    ratios = (('buy', 100), ('sell', 85), ('sell', 90), ('sell', 100))
    hilight_ratio = '90sell'
    hilight_depth = 2000
    include_stack = True

    def get_context_data(self, **kwargs):
        context = {}
        context['time'] = timezone.now()
        context['url_path'] = self.request.path

        self.get_api_data()

        table = self.init_table().get_table()

        table['hilight_cols'] = [self.hilight_ratio]
        table['hilight_rows'] = [self.hilight_depth]
        table['include_stack'] = self.include_stack

        context['table'] = table

        context['hilight_depth'] = self.hilight_depth
        context['hilight_price'] = table['data'][self.hilight_ratio][self.hilight_depth]
        if "item_data" in dir(self):
            context['item_name'] = self.item_data['name']
            context['item_icon'] = self.item_data['icon']

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return render(
            request,
            self.template_name,
            context,
        )