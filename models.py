# encoding: utf-8
from django.db import models

# TODO Dokumentumok osztály a képekkel összevonni?
# TODO A konferenciaelőadásokat végiggondolni.
# TODO Helyszínekhez földrajzi koordináták?

def kepek(instance, filename):
    return "kepek/%s" % filename
def dokumentumok(instance, filename):
    return "dokumentumok/%s" % filename

class Telepules(models.Model):
    class Meta:
        verbose_name=u"település"
        verbose_name_plural=u"települések"
        ordering = ['nev']

    def __unicode__(self):
        return self.nev
    megyek = list(enumerate((
        "Budapest", "Pest", "Fejér", "Komárom-Esztergom",
        "Veszprém", "Győr-Moson-Sopron", "Vas", "Zala",
        "Baranya", "Somogy", "Tolna", "Borsod-Abaúj-Zemplén",
        "Heves", "Nógrád", "Hajdú-Bihar",
        "Jász-Nagykun-Szolnok", "Szabolcs-Szatmár-Bereg",
        "Bács-Kiskun", "Békés", "Csongrád",
        "Ausztria", "Románia", "Szlovákia", "Ukrajna", "Horvátország", "Szerbia", "Szlovénia",
        "nem szomszédos ország",
        )))
    nev = models.CharField("település neve", max_length=100, unique=True)
    megye = models.IntegerField("megye (vagy ország)", choices=megyek, blank=True, null=True,
            help_text="Magyar településeknél válassza ki a megyét, szomszédos országoknál az ország nevét, más esetekben a \"nem szomszédos ország\" lehetőséget. <br>\nAz utóbbi esetben a település neve után írhatja az ország nevét vesszővel elválasztva.")
    longitude = models.FloatField("földrajzi hosszúság", blank=True, null=True)
    latitude = models.FloatField("földrajzi szélesség", blank=True, null=True)

class Dokumentum(models.Model):
    class Meta:
        verbose_name=u"dokumentum"
        verbose_name_plural=u"dokumentumok"
        ordering = ['nev']
    def __unicode__(self):
        return u"{0} ({1})".format(self.cim, self.nev)
#TODO nev->file vagy dokumentum
    nev = models.FileField('dokumentum', upload_to=dokumentumok)
    cim = models.CharField('dokumentum címe', max_length=100, blank=True)
    leiras = models.TextField("leírás",
        help_text="Ide írhat egy összefoglalást a dokumentumról. (Miről szól, rövid tartalom...)",
        blank=True)
    szemelyek = models.ManyToManyField("Szemely",
            verbose_name=u"személyek",
            help_text="Személyek, akik a dokumentumhoz köthetőek. Például a szerzője, vagy akiről szól.",
            blank=True
            )
    eloadasok = models.ManyToManyField("Esemeny",
            verbose_name=u"események",
            help_text="Események, amelyeknek a dokumentumhoz közük van.",
            blank=True
            )
    helyszinek = models.ManyToManyField("Helyszin",
            verbose_name=u"helyszínek",
            help_text="A helyszínek, amelyeknek a dokumentumhoz közük van.",
            blank=True
            )
    szervezetek = models.ManyToManyField("Szervezet",
            verbose_name=u"szervezetek",
            help_text="A szervezetek, amelyeknek a dokumentumhoz közük van.",
            blank=True
            )

class Kep(models.Model):
    class Meta:
        verbose_name=u"kép"
        verbose_name_plural=u"képek"
        ordering = ['cim']
    def __unicode__(self):
        return self.cim
    kep = models.ImageField('kép', upload_to=kepek)
    cim = models.CharField('kép címe', max_length=100, blank=True)
    leiras = models.TextField("leírás",
        help_text="Ide írhat egy összefoglalást a képről. (Mi szerepel rajta, érdekességek...)",
        blank=True)
    szemelyek = models.ManyToManyField("Szemely",
            verbose_name=u"személyek",
            help_text="A személyek, akik a képen szerepelnek, vagy a képhez közük van.",
            blank=True
            )
    eloadasok = models.ManyToManyField("Esemeny",
            verbose_name=u"események",
            help_text="Események, amelyek a képen szerepelnek, vagy a képhez közük van.",
            blank=True
            )
    helyszinek = models.ManyToManyField("Helyszin",
            verbose_name=u"helyszínek",
            help_text="A helyszínek, amelyek a képen szerepelnek, vagy a képhez közük van.",
            blank=True
            )
    szervezetek = models.ManyToManyField("Szervezet",
            verbose_name=u"szervezetek",
            help_text="A szervezetek, amelyeknek a képhez közük van.",
            blank=True
            )

class Helyszin(models.Model):
    class Meta:
        verbose_name=u"helyszín"
        verbose_name_plural=u"helyszínek"
        ordering = ['nev']
    def __unicode__(self):
        return self.nev
    nev = models.CharField("Jelenlegi név", max_length=100, unique=True,
        help_text="Ez jelenik meg a helyszín oldalán. Az előadásoknál megjelenő névváltozatok (névváltozási, címváltozás) más táblában szerepelnek.")
    leiras = models.TextField("leírás",
        help_text="Ide írhat egy összefoglalást a helyszínről. (Megközelítés, honlap, kapcsolati információk...)",
        blank=True)
    telepules = models.ForeignKey(Telepules, verbose_name="település")
    iranyitoszam = models.IntegerField("irányítószám", blank=True, null=True)
    email = models.EmailField('e-mail címe', max_length=100, blank=True,
        help_text="Az aktuális e-mailcíme. A helyszín honlapján jelenik meg.")
    fokep = models.ForeignKey("Kep",
        verbose_name='elsődleges kép a helyszínről',
        help_text = "Ez a kép fog megjelenni a helyszín oldalán a főrészben.",
        blank=True, null=True,
        )

class Helyszinnev(models.Model):
    class Meta:
        verbose_name=u"helyszínnév"
        verbose_name_plural=u"helyszínnevek"
        ordering = ['nev']
    def __unicode__(self):
        return "%s, %s" % (self.nev, self.cim)
    helyszin = models.ForeignKey(Helyszin, verbose_name="település")
    nev = models.CharField("Helyszín neve", max_length=200)
    cim  = models.CharField("Helyszín címe", max_length=200)

class Kategoria(models.Model):
    class Meta:
        verbose_name=u"kategória"
        verbose_name_plural=u"kategóriák"
        ordering = ['kategoria']
    def __unicode__(self):
        return self.kategoria
    kategoria = models.CharField('kategória', max_length=60)

class Szemely(models.Model):
    class Meta:
        verbose_name=u"személy"
        verbose_name_plural=u"személyek"
        ordering = ['nev']
    def __unicode__(self):
        return self.nev
    nev = models.CharField('személy neve', max_length=200, unique=True,
        help_text="Ez csak azonosításra szolgál. A honlapon megjelenő névváltozatok (doktorral vagy anélkül, lánykori vagy házas) más táblában szerepelnek.")
    leiras = models.TextField("leírás",
        help_text="Ide írhat egy összefoglalást a személyről. (Munkahelyek, kitüntetések, eredmények...)",
        blank=True)
    email = models.EmailField('e-mail címe', max_length=60, blank=True,
        help_text="Az pillanatnyilag érvényben lévő címe.")
    nyilvanosemail = models.BooleanField("nyilvános email?",
        help_text = "Akkor állítsuk igaz értékre, ha nem bejelentkezett felhasználók is láthatják. Ekkor megjelenik a személy adatlapján.",
        default=False)
    honlap = models.URLField(max_length=256,
        help_text = "A személy honlapja, ez megjelenik az adatlapján.",
        blank = True
        )
    arckep = models.ForeignKey("Kep",
        verbose_name='előadó arcképe',
        help_text = "Ez a kép fog megjelenni a személy oldalán a főrészben.",
        blank=True, null=True,
        )

class Szemelynev(models.Model):
    class Meta:
        verbose_name=u"személynév"
        verbose_name_plural=u"személynevek"
        ordering = ['nevvaltozat']
    def __unicode__(self):
        return "%s, %s" % (self.nevvaltozat, self.titulus)
    szemely = models.ForeignKey(Szemely, verbose_name="személy")
    nevvaltozat = models.CharField('előadó neve', max_length=200)
    titulus =  models.CharField('előadó titulusa', max_length=200,
        help_text="Ami a neve mellett megjelenik egy előadás vagy más esetén.")

class Szervezet(models.Model):
    class Meta:
        verbose_name=u"szervezet"
        verbose_name_plural=u"szervezetek"
        ordering = ['nev']
    def __unicode__(self):
        return self.nev
    nev = models.CharField("szervezet jelenlegi neve", max_length=200, unique=True,
        help_text="Ami a neve mellett megjelenik a szervezet oldalán.")
    szulo = models.ManyToManyField("self",
        blank=True, null=True,
        verbose_name="szülő szervezet",
        help_text="Amely szervezetnek része a szervezet. Pl. Az ELFT Fejér Megyei Csoport szülője az ELFT.")
    telepules = models.ForeignKey(Telepules,
        blank=True, null=True,
        verbose_name="település",
        )
    honlap = models.URLField("honlap", max_length=256, blank=True)
    logo = models.ForeignKey("Kep",
        verbose_name=u'logó',
        help_text = u"Logo, vagy más a szervezetre jellemző kép. Ez a kép fog megjelenni a szervezet oldalán a főrészben.",
        blank=True, null=True,
        )

class Szervezetnev(models.Model):
    class Meta:
        verbose_name=u"szervezetnév"
        verbose_name_plural=u"szervezetnevek"
        ordering = ['nevvaltozat']
    def __unicode__(self):
        return self.nevvaltozat
    szervezet = models.ForeignKey(Szervezet, verbose_name="szervezet")
    nevvaltozat = models.CharField('szervezet neve eseményekben', max_length=200,
        help_text="Ami a neve mellett megjelenik egy előadás vagy más esetén.")

class Esemeny(models.Model):
    class Meta:
        verbose_name=u"esemény"
        verbose_name_plural=u"események"
        ordering = ['nev']
    def __unicode__(self):
        return self.nev
    tipusok = (
            (u"előadás", "Önálló előadás"),
            (u"ülés", "Társulati ülés"),
            (u"verseny", "Verseny"),
            (u"konf", "Konferencia"),
            (u"csill", "Csillagászati esemény"),
            (u"műhely", "Diákműhely"),
    )
    nev =  models.CharField("esemény neve", max_length=200,
        help_text="Ilyen néven jelenik meg az eseménynaptárban.")
    tipus = models.CharField("esemény típusa", choices=tipusok,
        max_length=10)
    datum = models.DateField('dátuma',
            help_text="Több napos eseménynél a kezdőnap dátuma.")
    ido = models.TimeField('időpontja',
            blank=True, null=True,
            help_text="A kezdetének az időpontja.")
    vegdatum = models.DateField('befejezés dátuma',
            help_text="Több napos eseménynél a befejező nap dátuma.",
            blank=True, null=True,
            )
    vegido = models.TimeField('befejezés időpontja',
            blank=True, null=True,
            )

class Eloadas(Esemeny):
    """Önálló előadás. Nem konferencián vagy tárulati ülésen elhangzó."""
    class Meta:
        verbose_name=u"előadás"
        verbose_name_plural=u"előadások"
    def __unicode__(self):
        return "%s, %s" % (self.nev, self.datum)
    def save(self, *args, **kwargs):
        self.tipus = u"előadás"
        super(Eloadas, self).save(*args, **kwargs)
    eloado = models.ManyToManyField(Szemelynev,
        verbose_name="előadó",
        blank=True,
        )
    helyszin = models.ForeignKey(Helyszinnev,
        verbose_name="helyszín",
        )
    terem = models.CharField(max_length=50, blank=True)
    leiras = models.TextField(u"leírás", help_text=u"Ide írhat egy rövid összefoglalást az előadásról.", blank=True)
    meghivo = models.ForeignKey("Dokumentum",
        verbose_name=u"meghívó",
        help_text=u"Tipikusan az a fájl, amelyből az előadás plakátja készült.",
        blank=True, null=True,
        )
    kategoriak = models.ManyToManyField(Kategoria, blank=True,
        verbose_name="kategóriák",
        )
    szervezok = models.ManyToManyField(Szervezetnev, blank=True,
        verbose_name="szervezők",
        help_text=u"Szervező szervezetek nevei.",
        )
    letszam = models.IntegerField("létszám",
        help_text=u"A résztvevők létszáma az előadó(k) nélkül.",
        blank=True, null=True)
    kep = models.ForeignKey("Kep",
        verbose_name=u'címkép',
        help_text = u"Ez a kép fog megjelenni az események listájánál kicsiben és az előadás oldalán nagyban.",
        blank=True, null=True,
        )
    url = models.URLField("honlap",
        help_text=u"A honlap, ahol az eseményről többet lehet megtudni.",
        blank=True, null=True)


class Ules(Esemeny):
    """Társulati vagy más ülés."""
    class Meta:
        verbose_name=u"ülés"
        verbose_name_plural=u"ülések"
    def save(self, *args, **kwargs):
        self.tipus = u"ülés"
        super(Ules, self).save(*args, **kwargs)
    def __unicode__(self):
        return "%s, %s" % (self.nev, self.datum)
    helyszin = models.ForeignKey(Helyszinnev,
        verbose_name="helyszín",
        )
    terem = models.CharField(max_length=80, blank=True)
    leiras = models.TextField("leírás", help_text="Ide írhat egy rövid összefoglalást az előadásról.", blank=True)
    meghivo = models.ForeignKey("Dokumentum",
        verbose_name="meghívó fájl",
        help_text="Tipikusan az a fájl, amelyből az előadás plakátja készült.",
        blank=True, null=True,
        )
    jegyzokonyv = models.ForeignKey("Dokumentum",
        verbose_name="jegyzőkőnyv",
        help_text="Az ülésről készült jegyzőkönyv.",
        blank=True, null=True,
        related_name="jegyzokonyv_ulese",
        )
    eloado = models.ManyToManyField(Szemelynev,
        verbose_name="előadó",
        blank=True,
        )
    kategoriak = models.ManyToManyField(Kategoria, blank=True,
        verbose_name="kategóriák",
        )
    szervezet = models.ForeignKey(Szervezetnev,
        verbose_name="szervezet",
        help_text="Melyik szervezet ülése.",
        default = Szervezet.objects.get(nev__startswith="ELFT Fejér").id,
        )
    letszam = models.IntegerField("létszám",
        help_text="A résztvevők létszáma az előadó(k) nélkül.",
        blank=True, null=True)
    kep = models.ForeignKey("Kep",
        verbose_name=u'címkép',
        help_text = u"Ez a kép fog megjelenni az események listájánál kicsiben és az előadás oldalán nagyban.",
        blank=True, null=True,
        )
