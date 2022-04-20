from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('landing.urls', 'landing'), namespace='landing')),
    path('', include(('account.urls', 'account'), namespace='account')),
    path('stats/', include(('stats.urls', 'stats'), namespace='stats')),
]
