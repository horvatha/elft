from django.conf.urls.defaults import patterns, url
from arekdjango.elft.models import Esemeny

info_dict = {
        'queryset': Esemeny.objects.all().order_by("-datum")
}

urlpatterns = patterns('',

    (r'^$',  'arekdjango.elft.views.elft'),
    (r'^naptar/$',  'django.views.generic.list_detail.object_list', info_dict),
    (r'^naptar/(?P<year>\d+)/$',  'arekdjango.elft.views.year'),
    (r'^esemeny/(?P<object_id>\d+)/$',  'django.views.generic.list_detail.object_detail', info_dict),
    (r'^szemely/(?P<object_id>\d+)/$',  'arekdjango.elft.views.szemely'),
)

