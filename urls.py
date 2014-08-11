from django.conf.urls import patterns, url
from elft.models import Esemeny

info_dict = {
    'queryset': Esemeny.objects.all().order_by("-datum")
}

urlpatterns = patterns(
    '',
    url(r'^$',  'elft.views.main', name='main'),
    url(r'naptar/$',  'elft.views.main'),
    url(r'^naptar/(?P<year>\d+)/$',  'elft.views.year', name='year'),
    url(r'^esemeny/(?P<object_id>\d+)/$',  'elft.views.event', name='event'),
    url(r'^esemeny/(?P<object_id>\d+)/leiras$',
        'elft.views.event_description', name='event_description'),
    url(r'^szemely/(?P<object_id>\d+)/$',  'elft.views.szemely', name='person'),
    url(r'^szemely/$',  'elft.views.szemelyek', name='person_list'),
    url(r'^kategoria/(?P<object_id>\d+)/$',  'elft.views.category', name='category'),
    url(r'^kategoria/$',  'elft.views.categories', name='category_list'),
)
