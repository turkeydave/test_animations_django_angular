
from django.conf import settings
from django.conf.urls import patterns, url, include


urlpatterns = patterns(
    '',

    # These serve up static content via Django
    # In production nginx should be configured to serve it up
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.PROJECT_PATH + "/test_animations_app/css"}),
    url(r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.PROJECT_PATH + "/test_animations_app/images"}),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.PROJECT_PATH + "/test_animations_app/js"}),
    url(r'^vendor/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.PROJECT_PATH + "/test_animations_app/vendor"}),
    url(r'^partials/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.PROJECT_PATH + "/test_animations_app/partials"}),

    # Use this line if you want to test your environment with fully built and optimized js
    # Comment out the line above that conflicts
    # url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.PROJECT_PATH + "/build/js"}),

    # Promo URLs
    (r'^$', 'test_animations_app.views.index'),
    # (r'^index.html$', 'theo.views.promo_views.index'),
    # (r'^ordering/$', 'theo.views.promo_views.ordering'),
    # (r'^lotmanager/$', 'theo.views.promo_views.lotmanager'),
    # (r'^uptrade/$', 'theo.views.promo_views.uptrade'),
    # (r'^manufacturer/$', 'theo.views.promo_views.manufacturer'),
    # (r'^aboutus/$', 'theo.views.promo_views.aboutus'),
    # (r'^legal/$', 'theo.views.promo_views.legal'),
    # (r'^contactus/$', 'theo.views.promo_views.contactus'),
    # (r'^robots\.txt$', 'theo.views.promo_views.robots'),
)

if settings.USE_JASMINE:
    urlpatterns.append(
        url(r'^jasmine/', include('django_jasmine.urls')))


# from django.contrib import admin
# admin.autodiscover()
#
# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'test_animations.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#
#     url(r'^admin/', include(admin.site.urls)),
# )
