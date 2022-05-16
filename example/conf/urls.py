from django.urls import include, re_path
from django.contrib import admin

from organizations.backends import invitation_backend, registration_backend

admin.autodiscover()


urlpatterns = [
    re_path(r'^admin/', include(admin.site.urls)),
    re_path(r'^organizations/', include('organizations.urls')),
    re_path(r'^invite/', include(invitation_backend().get_urls())),
    re_path(r'^register/', include(registration_backend().get_urls())),
]
