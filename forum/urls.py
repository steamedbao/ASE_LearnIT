from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path, reverse

from apps.questions.views.questions import IndexView

urlpatterns = [
    path('admin', admin.site.urls),

    path('', IndexView.as_view(), name='index'),
    path('search', IndexView.as_view(), name='search'),

    path('', include('apps.accounts.urls')),
    path('', include('apps.questions.urls')),

]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path('__debug__', include(debug_toolbar.urls)),)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
