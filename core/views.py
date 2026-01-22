from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import get_resolver, URLPattern, URLResolver
from django.conf import settings

class CoreHomeView(APIView):
    """
    API Home: lists all available API endpoints with
    clickable URLs and allowed HTTP methods.
    """

    STANDARD_METHODS = {"GET", "POST", "PUT", "PATCH", "DELETE"}

    def get(self, request):
        resolver = get_resolver()
        api_urls = []

        base_url = request.build_absolute_uri('/').rstrip('/')

        def extract_methods(callback):
            methods = set()

            # ViewSet (router)
            if hasattr(callback, 'cls'):
                view_cls = callback.cls
                if hasattr(view_cls, 'http_method_names'):
                    methods.update(
                        m.upper() for m in view_cls.http_method_names
                        if m != 'options'
                    )

            # Function-based view
            elif hasattr(callback, 'methods'):
                methods.update(
                    m.upper() for m in callback.methods
                    if m != 'OPTIONS'
                )

            return list(methods & self.STANDARD_METHODS) or ["GET"]

        def list_urls(urlpatterns, prefix=''):
            for entry in urlpatterns:
                if isinstance(entry, URLResolver):
                    list_urls(entry.url_patterns, prefix + str(entry.pattern))

                elif isinstance(entry, URLPattern):
                    raw_path = prefix + str(entry.pattern)

                    if not raw_path.startswith('api/'):
                        continue

                    # Clean DRF-style paths
                    path = raw_path
                    path = path.replace('^', '').replace('$', '')
                    path = path.replace('<drf_format_suffix:format>', '')
                    path = path.replace('(?P<pk>[^/.]+)', '{id}')
                    path = path.replace('<int:pk>', '{id}')

                    full_url = f"{base_url}/{path}".replace(':/', '://').replace('//', '/')

                    methods = extract_methods(entry.callback)
                    # 🚫 Skip DRF format suffix regex URLs
                    if 'format' in path or '(?P<' in path:
                        continue

                    api_urls.append({
                        "path": f"/{path}",
                        "url": full_url,
                        "methods": methods
                    })

        list_urls(resolver.url_patterns)

        # Remove duplicates
        unique = {(u["path"], tuple(u["methods"])): u for u in api_urls}.values()

        return Response({
            "service": "core",
            "status": "running",
            "api_count": len(unique),
            "api_endpoints": sorted(unique, key=lambda x: x["path"])
        })
