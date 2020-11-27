from django.contrib import admin
from django.urls import path, include
from django.conf import settings #導入settings
from django.conf.urls.static import static #導入static
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('admin/', admin.site.urls),
    path('ckeditor',include('ckeditor_uploader.urls')), #引入路徑
    path('blog/', include('blog.urls')), #導入應用中設置的路徑
    path('comment/',include('comment.urls')),
    path('likes/',include('likes.urls')),
    path('user/', include('user.urls')),
    path('course/', include('course.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #導入路徑