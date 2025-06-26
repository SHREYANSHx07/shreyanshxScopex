"""
URL configuration for admin_dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('accounts:login')),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', lambda request: redirect('accounts:dashboard')),
    path('projects/', include('projects.urls')),
    path('tasks/', include('tasks.urls')),
    path('api/', include('accounts.api_urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('grappelli/', include('grappelli.urls')),  # for grappelli
#     path('admin/', admin.site.urls),
# ]
# from django.shortcuts import redirect

# urlpatterns = [
#     path('', lambda request: redirect('/admin/')),
#     path('grappelli/', include('grappelli.urls')),
#     path('admin/', admin.site.urls),
# ]
# from django.shortcuts import redirect
# from django.urls import path, include

# urlpatterns = [
#     path('grappelli/', include('grappelli.urls')),
#     path('admin/', admin.site.urls),
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('', lambda request: redirect('/admin/')),  # Root redirect
# ]