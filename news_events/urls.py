from django.contrib import admin
from django.urls import path, include
from news import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.home, name='home'),
                  path('accounts/', include('accounts.urls')),
                  path('news/', include('news.urls')),
                  path('events/', include('events.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
