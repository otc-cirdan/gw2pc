import re
import requests
from django.shortcuts import render


class GuildWars2APIMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, *args, **kwargs):
        whitelist = (
            'gw2pc_homepage',
            'about',
            'docs',
            'sitemap',
            'robots.txt',
        )

        if request.resolver_match.url_name not in whitelist:
            api_response = requests.get("https://api.guildwars2.com")

            if api_response.status_code == 503:
                # Extract error message using regex
                error_pattern = r"<p>(.*?)</p>"
                error_match = re.search(error_pattern, api_response.text, re.DOTALL)
                error_message = error_match.group(1) if error_match else "Unknown error"

                # Load the template and render it with the error message
                context = {'error_message': error_message}
                return render(
                    request,
                    "gw2pc/api_error.html",
                    context,
                    status=503,
                )
