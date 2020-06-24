from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('ask_a_question.urls')),
    path('api/', include('test_panel.urls')),
    path('api/', include('contacts.urls')),
    path('api/', include('education.urls')),
    path('api/', include('reviews.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
