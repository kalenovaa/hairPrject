from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from posts.views import html_view, login_view, sign_in
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('/test', test_view),
    path('', html_view),
    path('login/', login_view),
    path('sign_in/', sign_in),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
