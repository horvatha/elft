# encoding: utf-8
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response
from models import Szemely
import time

def elft(request):
    return HttpResponse("""Itt lesz az ELFT Fejér Megyei Szervezetének főoldala.
    <br/> <a href="naptar">Eseménynaptár</a>""")

def szemely(request, object_id):
    szemely = Szemely.objects.get(id=object_id)
    szemelynevek = szemely.szemelynev_set.all()
    eloadasok = []
    for szemelynev in szemelynevek:
        eloadasok.extend(szemelynev.eloadas_set.all())
    r = u"<h1>{0} oldala</h1>\n".format(szemely.nev)
    r += u"{0}\n</br>\n".format(szemely.leiras)
    r += u"Előadásai az adatbázisunkban:\n<ul>\n"
    for eloadas in eloadasok:
            r += u" <li>{0}</li>\n".format(eloadas.nev)
    r += "</ul>"

    return HttpResponse(r)

def year(request, year):
    year = int(year)
    thisyear = time.localtime().tm_year
    maxyear = thisyear + 1
    if  not 1970 <= year <= maxyear:
        return HttpResponseNotFound(u'<h1>{year} kívül esik a tárolt tartományból (1970-{maxyear})</h1>'.format(
            year=year,
            maxyear=maxyear,
            ))
    return HttpResponse(u"<h1>Itt lesznek a %s év eseményei</h1>" % year)
