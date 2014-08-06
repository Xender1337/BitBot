from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import Trade.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BitBot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',      include(Trade.urls)),
    url(r'^trade/', include(Trade.urls)),
    url(r'^Trade/', include(Trade.urls)),
)
