from django.contrib import admin
from django.urls import path, include
from store import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='store/home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('figures/', views.figure_list, name='figure_list'),
    path('figures/<slug:slug>/', views.figure_detail, name='figure_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)