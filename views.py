# encoding: utf-8
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response
from models import Szemely, Esemeny, Kategoria
import datetime

min_year = 1970


def main(request):
    today = datetime.date.today()
    # enddate = today + datetime.timedelta(days=6)
    this_year = today.year
    next_events = Esemeny.objects.filter(datum__gte=today).order_by("datum")
    all_events = Esemeny.objects.all()
    year_count = {}
    all_count = 0
    for year in range(min_year, this_year+2):
        year_count[year] = 0
    for event in all_events:
        year_count[event.datum.year] += 1
        all_count += 1
    year_count = [{"year": year, "count": year_count[year]}
                  for year in range(min_year, this_year+2)
                  if year_count[year] != 0
                  ]

    return render_to_response(
        "elft/main.html",
        {
            "idei_ev": this_year,
            "esemenyek": next_events,
            "year_count": year_count,
            "all_count": all_count,
        }
    )


def szemelyek(request):
    szemelyek = Szemely.objects.all()
    return render_to_response(
        "elft/person_list.html",
        {
            "persons": szemelyek,
        }
    )


def szemely(request, object_id):
    szemely = Szemely.objects.get(id=object_id)
    szemelynevek = szemely.szemelynev_set.all()
    events = []
    for szemelynev in szemelynevek:
        events.extend(szemelynev.eloadas_set.all().order_by("-datum"))
        events.extend(szemelynev.ules_set.all().order_by("-datum"))

    return render_to_response(
        "elft/person.html",
        {
            "szemely": szemely,
            "esemenyek": events,
        }
    )


def categories(request):
    kategoriak = Kategoria.objects.all()
    return render_to_response(
        "elft/category_list.html",
        {
            "categories": kategoriak,
        }
    )


def category(request, object_id):
    category = Kategoria.objects.get(id=object_id)
    lessions = category.eloadas_set.all()
    ulesek = category.ules_set.all()

    return render_to_response(
        "elft/category.html",
        {
            "kategoria": category,
            "eloadasok": lessions,
            "ulesek": ulesek,
        }
    )


def event(request, object_id):
    event = Esemeny.objects.get(id=object_id)
    return render_to_response(
        "elft/esemeny_detail.html",
        {
            "esemeny": event,
        }
    )


def event_description(request, object_id):
    event = Esemeny.objects.get(id=object_id)
    if event.tipus == u"előadás" and event.eloadas.leiras:
        return HttpResponse(event.eloadas.leiras, "text/plain")
    else:
        return HttpResponseNotFound(u"Nem tartozik leírás az eseményhez.")


def year(request, year):
    year = int(year)
    max_year = datetime.date.today().year+1
    error_mesg = (u'<h1>{year} kívül esik a tárolt tartományból'
                  ' ({min_year}-{max_year})</h1>')
    if not min_year <= year <= max_year:
        return HttpResponseNotFound(
            error_mesg.format(
                year=year,
                max_year=max_year,
                min_year=min_year,
            )
        )
    events = Esemeny.objects.filter(datum__year=year).order_by("datum")
    previous_year = year-1 if year > min_year else None
    next_year = year+1 if year < max_year else None
    return render_to_response(
        "elft/esemeny_list.html",
        {
            "events": events,
            "year": year,
            "previous_year": previous_year,
            "next_year": next_year,
        }
    )
