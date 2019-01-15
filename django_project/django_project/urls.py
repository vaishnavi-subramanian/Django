from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # /admin/
    path('admin/', admin.site.urls),

    # /blog/
    path('blog/', include('blog.urls', namespace='Blog')),

    # /accounts/
    path('accounts/', include('accounts.urls', namespace='Accounts'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
