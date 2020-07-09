import os
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .settings import APPS_DIR, apps_dir_str

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.base.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

for app in os.listdir(APPS_DIR):
	new_path = path(f'{app}/', include(f'{apps_dir_str}.{app}.urls'))
	urlpatterns.append(new_path)