from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone


class ServicePage(models.Model):
    car = models.CharField('Model pojazdu', help_text='Wprowadź model pojazdu który będzie wyświetlony nad tabelą', max_length=500)

    def __str__(self):
        return self.car

    class Meta:
        verbose_name = 'Tabele strony usług'
        verbose_name_plural = 'Tabele strony usług'


class ServiceTable(models.Model):
    servicetable = models.ForeignKey(ServicePage, on_delete=models.CASCADE, related_name="servicetable")
    service_name = models.CharField('Nazwa usługi', help_text='Wprowadź nazwę usługi', max_length=800)
    service_price = models.CharField('Cena usługi', help_text='Wprowadź cenę usługi', max_length=800)

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = 'Wiersz tabeli'
        verbose_name_plural = 'Wiersze tabeli'


class Service(models.Model):
    image = models.ImageField('Zdjecie bloku', upload_to='service_images', help_text='Wybierz zdjęcie', null=True,blank=True)
    title = models.CharField('Tytuł bloku', null=True, blank=True, max_length=700)
    desc = models.TextField('Zawartość bloku', null=True, blank=True)
    CHOICES = (
        ("Zdjęcie po lewej", "Zdjęcie po lewej"),
        ("Zdjęcie po prawej", "Zdjęcie po prawej"),
    )
    choise = models.CharField(max_length=100, choices=CHOICES, default="Zdjęcie po lewej")
    my_order = models.PositiveIntegerField('Sortowanie', default=0, blank=False, null=False)
    url = models.CharField('Link do podstrony', null=True, blank=True, max_length=200)

    def __str__(self):
        return self.title

    class Meta(object):
        ordering = ['my_order']
        verbose_name = 'Usługi'
        verbose_name_plural = 'Usługi'


class Car(models.Model):
    model = models.CharField('Model samochodu', max_length=200)
    month_price = models.IntegerField('Cena (miesięcznie)')
    price = models.IntegerField('Cena za wynajem (dziennie)')
    promotion = models.IntegerField('Promocja (w %)', help_text='W procentach (%)', null=True, blank=True)
    non_working_hours = models.IntegerField('Wynajem / zwrot auta poza godzinami pracy biura', help_text='Cena', default=99)
    limit_per_day = models.CharField('Limit dziennie', max_length=10, default='200 km')
    limit_per_week = models.CharField('Limit tygodniowo', max_length=10, default='1 400 km')
    limit_per_two_weeks = models.CharField('Limit dwa tygodnie', max_length=10, default='2 100 km')
    limit_per_month = models.CharField('Limit miesięcznie', max_length=10, default='3 000 km')
    limit_per_year = models.CharField('Limit rocznie', max_length=10, default='30 000 km')
    car_photo = models.ImageField('Zdjęcie samochodu', upload_to='car_image_small', help_text='Zdjecie samochodu', null=True, blank=True)
    about = models.TextField('Opis samochodu', null=True, blank=True)
    important_information = models.TextField('Ważne informacje', null=True, blank=True)
    deposit = models.CharField('Kaucja', max_length=20, blank=True, null=False)
    is_rent_deposit = models.BooleanField('Kaucja przy opłacie kartą?', default=False)
    rent_deposit = models.CharField('Kaucja przy opłacie kartą', max_length=20, blank=True, null=False)
    my_order = models.PositiveIntegerField('Porządek', default=0, blank=False, null=False)
    show_on_home = models.BooleanField('Wyświetlić na stronie głównej', default=False)
    disable = models.BooleanField('Nie wyświetlać auto na stronie', default=False)
    slug_car = models.SlugField('Link strony', unique=True)
    meta_title = models.CharField('Meta Title', max_length=200, blank=True, null=True)
    meta_description = models.CharField('Meta Description', max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.price = round(self.month_price / 30)
        super(Car, self).save(*args, **kwargs)
        return self.price

    def __str__(self):
        return self.model

    class Meta:
        ordering = ['-promotion', 'my_order']
        verbose_name = 'Samochód'
        verbose_name_plural = 'Samochody'


class CarDetailTables(models.Model):
    title = models.CharField('Kolumna', max_length=500, editable=False)
    desc = models.CharField('Text kolumny', max_length=500)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'Usuń wybranych' in actions:
            del actions['Usuń wybranych']
        return actions

    class Meta:
        verbose_name = 'Dodatkowa tabela strony auta'
        verbose_name_plural = 'Dodatkowe tabele strony auta'


class SliderImage(models.Model):
    slider_image = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='slider_images')
    image = models.ImageField('Zdjecie samochodu', upload_to='slider_images', help_text='Zdjecie samochodu', null=True, blank=True)

    class Meta:
        verbose_name = 'Sdjęcie samochodu'
        verbose_name_plural = 'Sdjęcia samochodu'


class RentPeriod(models.Model):
    period = models.CharField('Okres', max_length=50)
    period_from = models.IntegerField('Od', default=0)
    period_to = models.IntegerField('Do', default=0)

    def __str__(self):
        return self.period

    class Meta:
        verbose_name = 'Okres wynajmu'
        verbose_name_plural = 'Okres wynajmu'


class CarRentPeriod(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='periods')
    period = models.ForeignKey(RentPeriod, on_delete=models.CASCADE, max_length=50)
    price = models.IntegerField('Cena')
    text = models.CharField('Tekst po liczbie', max_length=50)
    limit = models.IntegerField('Limit km dziennie', default=200)


class Option(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='options')
    option = models.CharField('Wyposażenie', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.option

    class Meta:
        verbose_name = 'Wyposażenie samochodu'
        verbose_name_plural = 'Wyposażenia samochodu'


class Post(models.Model):
    image_small = models.ImageField('Obraz podglądu', blank=True, null=True, upload_to='posts')
    image_big = models.ImageField('Obraz artykułu', blank=True, null=True, upload_to='posts')
    title = models.CharField('Nazwa artykułu', max_length=100)
    short_desc = models.TextField('Krótki opis', max_length=700)
    full_desc = models.TextField('Zawartosć artykułu')
    date = models.DateField('Data', auto_now=False)
    slug_posts = models.SlugField(default='slug', unique=True)

    def save(self, *args, **kwargs):
        self.slug_posts = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Wpis'
        verbose_name_plural = 'Wpisy'


class MainSLider(models.Model):
    title = models.CharField('Tytuł duży', null=False, blank=True, max_length=1500)
    sub_title = models.TextField('Tytuł mały', null=False, blank=True, max_length=1500)
    images = models.ImageField('Zdjęcie', upload_to='main_slider', null=False, blank=True)
    button_1 = models.CharField('Tekst pierwszego przycisku', null=False, blank=True, max_length=500)
    button_2 = models.CharField('Tekst drugiego przycisku', null=False, blank=True, max_length=500)
    link_1 = models.CharField('Link pierwszego przycisku', null=False, blank=True, max_length=800)
    link_2 = models.CharField('Link drugiego przycisku', null=False, blank=True, max_length=800)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Slider(Strona główna)'
        verbose_name_plural = 'Slider(Strona główna)'


class Subscriber(models.Model):
    email = models.EmailField()
    date = models.DateField(default=timezone.now, editable=False)

    def __str__(self):
        return self.email


class ExtraOptions(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_key')
    title = models.CharField('Opcja', null=True, blank=True, max_length=3000)
    desc = models.CharField('Opis opcji', null=True, blank=True, max_length=2000)
    price = models.CharField('Cena', null=True, blank=True, max_length=100)
    CHOICES = (
        ("W cenie", "W cenie"),
        ("Dodatkowa cena", "Dodatkowa cena"),
    )
    choise = models.CharField('Rodzaj ceny', max_length=100, choices=CHOICES, default="Dodatkowa cena")
    CHOICES = (
        ("Cena za dobę", "Cena za dobę"),
        ("Cena pojedyncza", "Cena pojedyncza"),
    )
    choise_price = models.CharField('Naliczanie ceny', max_length=100, choices=CHOICES, default="Cena za dobę")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Opcja dodatkowa'
        verbose_name_plural = 'Opcje dodatkowe'
        ordering = ['car']
