from django.contrib import admin
from django.urls import path
from app.views import home, prod, contact, about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('product/', prod),
    path('contact/', contact),
    path('about/', about)

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

