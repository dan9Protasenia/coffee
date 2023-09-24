from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("__debug__/", include("debug_toolbar.urls")),
                  path('captcha/', include('captcha.urls')),
                  path('coffee/', include('project.apps.coffee.urls'))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)

    urlpatterns = [
                      path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
