Lehet, hogy már nem igaz az alábbi.

Az elft alkalmazás telepítése kicsit trükkös.
Az Ules osztályban van egy ilyen rész:

    szervezet = models.ForeignKey(Szervezetnev,
        verbose_name="szervezet",
        help_text="Melyik szervezet ülése.",
        default = Szervezet.objects.get(nev__startswith="ELFT Fejér").id,
        )

Tehát mielőtt az adatbázist először szinkronizáljuk,
megjegyzésbe kell rakni a default értéket,
szinkronizálni, létrehozni az ELFT Fejér kezdetű szervezetet,
és utána visszaállítani a default sort.
