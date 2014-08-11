from elft.models import (Helyszin, Helyszinnev, Telepules, Eloadas, Szemely,
                         Szemelynev, Kategoria, Szervezet, Szervezetnev,
                         Kep, Dokumentum, Ules)
from django.contrib import admin


class SzemelynevInline(admin.TabularInline):
    model = Szemelynev
    extra = 2


class SzemelyAdmin(admin.ModelAdmin):
    inlines = [SzemelynevInline]


class HelyszinnevInline(admin.TabularInline):
    model = Helyszinnev
    extra = 2


class HelyszinAdmin(admin.ModelAdmin):
    inlines = [HelyszinnevInline]


class SzervezetnevInline(admin.TabularInline):
    model = Szervezetnev
    extra = 2


class SzervezetAdmin(admin.ModelAdmin):
    inlines = [SzervezetnevInline]


class EsemenyAdmin(admin.ModelAdmin):
    exclude = ('tipus', )


admin.site.register(Telepules)
admin.site.register(Helyszin, HelyszinAdmin)
# admin.site.register(Helyszinnev)
# admin.site.register(Esemeny, EsemenyAdmin)
admin.site.register(Kategoria)
admin.site.register(Kep)
admin.site.register(Dokumentum)
admin.site.register(Szemely, SzemelyAdmin)
# admin.site.register(Szemelynev)
admin.site.register(Szervezet, SzervezetAdmin)
admin.site.register(Eloadas, EsemenyAdmin)
admin.site.register(Ules, EsemenyAdmin)
