from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('games/', include('games.urls'))
=======
    path('games/', include('games.urls')),
    path('game/', include('games.urls'))

>>>>>>> 984084a2207a36f6070aed74c596a38203909407
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
