"""shop_fox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import view_home
from django.views.generic import RedirectView

from django.views.static import serve
from django.urls import re_path as url

from catalog.views import SearchResultsView

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('image/favicon.ico'))),
    path('catalog/', include(('catalog.urls', 'catalog'), namespace='catalog')),
    path('cart/', include('cart.urls')),
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
    path('', view_home, name='home'),
    path('search/', SearchResultsView.as_view(), name="search_results",),
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

else:
    urlpatterns += [
        url(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
            serve, {'document_root': settings.MEDIA_ROOT}),
        url(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$',
            serve, {'document_root': settings.STATIC_ROOT}), ]
