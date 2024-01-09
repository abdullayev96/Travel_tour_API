from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

from django.conf.urls.static import static
from django.conf import settings

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Welcome to Best Tour API",
      default_version='developer96',
      description="note",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns  = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('api/contact/', include("contact.urls")),


]


urlpatterns += i18n_patterns(

    path('api/home/', include("home.urls")),
    path('api/card/', include("card.urls")),
    path('api/leader/', include("leader.urls")),
    path('api/comment/', include("opinion.urls")),



)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


###travel
##1234.