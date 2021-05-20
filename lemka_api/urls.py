from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Lemka API",
        default_version='v1',
        description="Ceci est l'API pour le site web https://www.lemka.be/",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@lemka.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/public/', include('lemka.urls')),
    path('api/', include('administrateur.urls')),
    path('api/profil/', include('utilisateur.urls')),
    path('api/auth/', include('authentication.urls')),
    path('api/auth-social/', include(('social_auth.urls', 'social_auth'), namespace="social_auth"))
    # path('api/', views.api_root),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
