from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import get_resolver, URLPattern, URLResolver

class CoreHomeView(APIView):
    """
    Home API that lists all API endpoints in a clean format,
    showing only standard HTTP methods (GET, POST, PUT, PATCH, DELETE).
    """

    STANDARD_METHODS = {"GET", "POST", "PUT", "PATCH", "DELETE"}

    def get(self, request):
        resolver = get_resolver()
        api_urls = []

        def list_urls(urlpatterns, prefix=''):
            for entry in urlpatterns:
                if isinstance(entry, URLResolver):
                    list_urls(entry.url_patterns, prefix + str(entry.pattern))
                elif isinstance(entry, URLPattern):
                    path = prefix + str(entry.pattern)
                    if path.startswith('api/'):
                        # Clean path: remove regex symbols
                        path = path.replace('^', '').replace('$', '').replace('\\.', '.')
                        path = path.replace('(?P<pk>[^/.]+)', '{id}')  # show {id} for clarity
                        path = path.replace('<drf_format_suffix:format>', '')  # remove DRF format suffix

                        # Get allowed methods
                        callback = entry.callback
                        methods = []
                        if hasattr(callback, 'cls'):  # class-based view
                            view_class = callback.cls
                            if hasattr(view_class, 'http_method_names'):
                                methods = [m.upper() for m in view_class.http_method_names if m != 'options']
                        else:
                            if hasattr(callback, 'methods'):
                                methods = [m.upper() for m in callback.methods if m != 'OPTIONS']

                        # Keep only standard methods
                        methods = [m for m in methods if m in self.STANDARD_METHODS]
                        if not methods:
                            methods = ["GET"]

                        api_urls.append({
                            "path": path,
                            "methods": methods
                        })

        list_urls(resolver.url_patterns)

        # Remove duplicates and sort
        unique_urls = {u['path']: u for u in api_urls}.values()
        sorted_urls = sorted(unique_urls, key=lambda x: x['path'])

        return Response({
            'service': 'core',
            'status': 'running',
            'api_endpoints': sorted_urls
        })
