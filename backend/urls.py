"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.http import JsonResponse
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.views.decorators.http import require_http_methods

admin.site.site_header = "KALRO Selector Administration"
admin.site.site_title = "KALRO Selector Admin"
admin.site.index_title = "Welcome to KALRO Selector Dashboard"

@require_http_methods(["GET"])
def root_view(request):
    base_url = f"{request.scheme}://{request.get_host()}"
    return JsonResponse({
        'message': 'Welcome to KALRO Selector Backend API',
        'base_url': base_url,
        'documentation': {
            'admin_panel': f'{base_url}/admin/',
            'api_root': f'{base_url}/api/',
            'note': 'All endpoints support GET (list/retrieve), POST (create), PUT/PATCH (update), DELETE operations'
        },
        'endpoints': {
            'counties': {
                'url': f'{base_url}/api/counties/',
                'methods': ['GET', 'POST'],
                'detail': f'{base_url}/api/counties/{{id}}/',
                'search': f'{base_url}/api/counties/?search=term',
                'description': 'List and manage counties'
            },
            'subcounties': {
                'url': f'{base_url}/api/subcounties/',
                'methods': ['GET', 'POST'],
                'detail': f'{base_url}/api/subcounties/{{id}}/',
                'search': f'{base_url}/api/subcounties/?search=term',
                'description': 'List and manage subcounties'
            },
            'wards': {
                'url': f'{base_url}/api/wards/',
                'methods': ['GET', 'POST'],
                'detail': f'{base_url}/api/wards/{{id}}/',
                'search': f'{base_url}/api/wards/?search=term',
                'description': 'List and manage wards'
            },
            'crop_categories': {
                'url': f'{base_url}/api/crop-categories/',
                'methods': ['GET', 'POST'],
                'detail': f'{base_url}/api/crop-categories/{{id}}/',
                'search': f'{base_url}/api/crop-categories/?search=term',
                'description': 'List and manage crop categories'
            },
            'crops': {
                'url': f'{base_url}/api/crops/',
                'methods': ['GET', 'POST'],
                'detail': f'{base_url}/api/crops/{{id}}/',
                'search': f'{base_url}/api/crops/?search=term',
                'description': 'List and manage crops'
            },
            'crop_varieties': {
                'url': f'{base_url}/api/crop-varieties/',
                'methods': ['GET', 'POST'],
                'detail': f'{base_url}/api/crop-varieties/{{id}}/',
                'search': f'{base_url}/api/crop-varieties/?search=term',
                'description': 'List and manage crop varieties'
            },
            'soil_types': {
                'url': f'{base_url}/api/soil-types/',
                'methods': ['GET', 'POST'],
                'detail': f'{base_url}/api/soil-types/{{id}}/',
                'search': f'{base_url}/api/soil-types/?search=term',
                'description': 'List and manage soil types'
            },
            'crop_soil_types': {
                'url': f'{base_url}/api/crop-soil-ypes/',
                'methods': ['GET', 'POST'],
                'detail': f'{base_url}/api/crop-soil-ypes/{{id}}/',
                'description': 'List and manage crop-soil type relationships'
            },
            'aez_zones': {
                'url': f'{base_url}/api/aez-zones/',
                'methods': ['GET', 'POST'],
                'detail': f'{base_url}/api/aez-zones/{{id}}/',
                'search': f'{base_url}/api/aez-zones/?search=term',
                'description': 'List and manage AEZ (Agro-Ecological Zone) zones'
            },
            'livestock_categories': {
                'url': f'{base_url}/api/livestock-categories/',
                'methods': ['GET', 'POST'],
                'detail': f'{base_url}/api/livestock-categories/{{id}}/',
                'search': f'{base_url}/api/livestock-categories/?search=term',
                'description': 'List and manage livestock categories'
            },
            'livestocks': {
                'url': f'{base_url}/api/livestocks/',
                'methods': ['GET', 'POST'],
                'detail': f'{base_url}/api/livestocks/{{id}}/',
                'search': f'{base_url}/api/livestocks/?search=term',
                'description': 'List and manage livestock breeds'
            },
            'pasture_categories': {
                'url': f'{base_url}/api/pasture-categories/',
                'methods': ['GET', 'POST'],
                'detail': f'{base_url}/api/pasture-categories/{{id}}/',
                'search': f'{base_url}/api/pasture-categories/?search=term',
                'description': 'List and manage pasture categories'
            },
            'pastures': {
                'url': f'{base_url}/api/pastures/',
                'methods': ['GET', 'POST'],
                'detail': f'{base_url}/api/pastures/{{id}}/',
                'search': f'{base_url}/api/pastures/?search=term',
                'description': 'List and manage pastures'
            },
            'pasture_varieties': {
                'url': f'{base_url}/api/pasture-varieties/',
                'methods': ['GET', 'POST'],
                'detail': f'{base_url}/api/pasture-varieties/{{id}}/',
                'search': f'{base_url}/api/pasture-varieties/?search=term',
                'description': 'List and manage pasture varieties'
            }
        },
        'usage_examples': {
            'get_all_counties': f'curl {base_url}/api/counties/',
            'get_single_county': f'curl {base_url}/api/counties/1/',
            'create_county': f'curl -X POST {base_url}/api/counties/ -H "Content-Type: application/json" -d \'{{"name":"County Name","county_id":"001"}}\'',
            'update_county': f'curl -X PUT {base_url}/api/counties/1/ -H "Content-Type: application/json" -d \'{{"name":"Updated Name"}}\'',
            'delete_county': f'curl -X DELETE {base_url}/api/counties/1/',
            'search': f'curl {base_url}/api/counties/?search=term'
        },
        'notes': [
            'Visit any endpoint with a browser to see the browsable API interface',
            'All endpoints support JSON format',
            'Use Content-Type: application/json header for POST/PUT/PATCH requests',
            'Search functionality is available on most endpoints using ?search=term parameter'
        ]
    })

urlpatterns = [
    path('', root_view, name='root'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]
