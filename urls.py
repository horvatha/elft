from django.conf.urls.defaults import patterns, url
from arekdjango.elft.models import Esemeny

info_dict = {
        'queryset': Esemeny.objects.all().order_by("-datum")
}

urlpatterns = patterns('',

    (r'^$',  'arekdjango.elft.views.main'),
    (r'naptar/$',  'arekdjango.elft.views.main'),
    #(r'^naptar/2013/$',  'django.views.generic.list_detail.object_list', info_dict),
    (r'^naptar/(?P<year>\d+)/$',  'arekdjango.elft.views.year'),
    (r'^esemeny/(?P<object_id>\d+)/$',  'arekdjango.elft.views.event'),
    (r'^esemeny/(?P<object_id>\d+)/leiras$',  'arekdjango.elft.views.event_description'),
    (r'^szemely/(?P<object_id>\d+)/$',  'arekdjango.elft.views.szemely'),
    (r'^szemely/$',  'arekdjango.elft.views.szemelyek'),
    (r'^kategoria/(?P<object_id>\d+)/$',  'arekdjango.elft.views.category'),
    (r'^kategoria/$',  'arekdjango.elft.views.categories'),
)

