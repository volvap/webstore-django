from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('',include('users.urls')),
    path('', include('polls.urls'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
