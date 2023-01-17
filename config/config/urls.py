from django.contrib import admin
from django.urls import path, include

from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api_2/', include('todo.urls')),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
    path('', include('books.urls', namespace='books')),
    path('openapi', get_schema_view(
            title="Blog API",
            description="A sample API for learning DRF",
            version="1.0.0"
        ), name='openapi-schema'),
]
