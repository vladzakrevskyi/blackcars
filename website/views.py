from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, EmptyPage
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from .models import *
from .form import *
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.template import loader, Context


def render_tamplate(tpl, dt, request):
    car_detail = list(CarDetailTables.objects.values_list('desc', flat=True))
    image = SliderImage.objects.all()
    option = Option.objects.all()
    dct = {'options': option, 'slider_images': image, 'car_detail': car_detail}
    dct.update(dt)
    return render(request, tpl, dct)


def contact_form(request):
    c_form = ContactForm(request.POST)

    if c_form.is_valid():
        name = c_form.cleaned_data['name']
        email = c_form.cleaned_data['email']
        phone = c_form.cleaned_data['phone']
        message = c_form.cleaned_data['message']
        recipients = ['office@blackcars.pl.test-google-a.com']

        try:
            send_mail("[BlackCars] Contact Form Message",
                      "Name: %s \nEmail: %s \nPhone: %s \n\nMessage: %s"
                      "\n\nPlease don't reply to this message. "
                      "For the answer use the e-mail specified by the client."
                      % (name, email, phone, message), 'office@blackcars.pl', recipients)
            send_mail(
                '[BlackCars] Dziękujemy za Twój kontakt',
                'Dziękujemy za Twój kontakt.\n'
                'Skontaktujemy się z Tobą w najbliższym czasie.\n'
                'Pozdrawiamy,\nZespół BlackCars.',
                'office@blackcars.pl',
                [c_form.cleaned_data['email']],
            )

        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return redirect('/success_page')


def newsletter_form(request):
    cc_form = NewsletterForm(request.POST)

    if cc_form.is_valid():
        name = cc_form.cleaned_data['name']
        email = cc_form.cleaned_data['email']
        phone = cc_form.cleaned_data['phone']
        message = cc_form.cleaned_data['message']
        recipients = ['office@blackcars.pl.test-google-a.com']

        try:
            send_mail("[BlackCars] Contact Form Message",
                      "Name: %s \nEmail: %s \nPhone: %s \n\nMessage: %s"
                      "\n\nPlease don't reply to this message. "
                      "For the answer use the e-mail specified by the client."
                      % (name, email, phone, message), 'office@blackcars.pl', recipients)
            send_mail(
                '[BlackCars] Dziękujemy za Twój kontakt',
                'Dziękujemy za Twój kontakt.\n'
                'Skontaktujemy się z Tobą w najbliższym czasie.\n'
                'Pozdrawiamy,\nZespół BlackCars.',
                'office@blackcars.pl',
                [cc_form.cleaned_data['email']],
            )

        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return redirect('/success_newsleter')


def home(request):
    slider = MainSLider.objects.all()
    cars = Car.objects.filter(show_on_home=True, disable=False)
    dct = {'slider': slider, 'cars': cars}
    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            email = newsletter_form.cleaned_data['email']
            recipients = ['office@blackcars.pl.test-google-a.com']
            e = Subscriber(email=email)
            e.save()
            try:
                send_mail("[BlackCars] Nowa subskrypcja",
                          "\nEmail: %s"
                          "\n\nPlease don't reply to this message. "
                          "For the answer use the e-mail specified by the client."
                          % (email), 'office@blackcars.pl', recipients)
                send_mail(
                    '[BlackCars] Dziękujemy za subskrypcje',
                    'Dziękujemy za subskrypcje.\n'
                    'Pozdrawiamy,\nZespół BlackCars.',
                    'office@blackcars.pl',
                    [newsletter_form.cleaned_data['email']],
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('/sukcess_newsletter')
        else:
            return render_tamplate("index.html", dct, request)
    else:
        return render_tamplate("index.html", dct, request)


def about(request):
    return render_tamplate("about.html", {}, request)


def our_cars(request):
    promotion_cars = Car.objects.filter(promotion__isnull=False, disable=False)
    cars = Car.objects.filter(promotion__isnull=True, disable=False)
    return render_tamplate("our_cars.html", {'promotion_cars': promotion_cars, 'cars': cars}, request)


def contact(request):
    if request.method == 'POST':
        c_form = ContactForm(request.POST)
        if c_form.is_valid():
            return contact_form(request)
        else:
            return render_tamplate('contact.html', {}, request)
    else:
        return render_tamplate('contact.html', {}, request)


def blog(request):
    posts = Post.objects.all().order_by('-date')
    p = Paginator(posts, 10)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    return render_tamplate("blog.html", {'posts': page}, request)


def blog_detail(request, post_slug):
    post = Post.objects.get(slug_posts=post_slug)
    return render_tamplate("blog_detail.html", {'post': post}, request)


def reservation_form(request):

    cc_form = ReservationForm(request.POST)

    if cc_form.is_valid():
        name = cc_form.cleaned_data['name']
        street = cc_form.cleaned_data['street']
        zip = cc_form.cleaned_data['zip']
        nip = cc_form.cleaned_data['nip']
        city = cc_form.cleaned_data['city']
        phone = cc_form.cleaned_data['phone']
        email = cc_form.cleaned_data['email']
        license = cc_form.cleaned_data['license']
        pesel = cc_form.cleaned_data['pesel']
        reservation_code = cc_form.cleaned_data['reservation_code']
        selected = request.POST.getlist('selected')
        price_day = cc_form.cleaned_data['price_day']
        extra_services = cc_form.cleaned_data['extra_services']
        pay = cc_form.cleaned_data['pay']
        card_number = cc_form.cleaned_data['card_number']
        card_month = cc_form.cleaned_data['card_month']
        card_year = cc_form.cleaned_data['card_year']
        card_cvv = cc_form.cleaned_data['card_cvv']
        car_name = cc_form.cleaned_data['car_name']
        date_start = cc_form.cleaned_data['date_start']
        date_end = cc_form.cleaned_data['date_end']
        limit_day = cc_form.cleaned_data['limit_day']
        actual_deposit = cc_form.cleaned_data['actual_deposit']
        rent_price = cc_form.cleaned_data['rent_price']
        rent_days = cc_form.cleaned_data['rent_days']
        final_price = cc_form.cleaned_data['final_price']
        text_pay = cc_form.cleaned_data['text_pay']
        remarks = cc_form.cleaned_data['remarks']
        recipients = ['office@blackcars.pl.test-google-a.com']
        # recipients = ['dmitry@gnuhost.eu']

        try:
            send_mail("[BlackCars] Nowa Rezerwacja",
                      "Nowa rezerwacja: \n\n\n"
                      "Wybrana metoda płatności: %s\n\n\n"
                      "Numer rezerwacji: %s\n"
                      "Auto: %s\n\n"
                      "Odbiór: %s\n"
                      "Zwrot: %s\n"
                      "Doby: %s\n"
                      "Cena za dobę: %s\n"
                      "Całkowity limit km: %s\n"
                      "Сena za wynajem lącznie: %s\n\n"
                      "Wybrane opcje dodatkowe:\n"
                      "%s\n"
                      "Opcje dodatkowe: %s\n\n"
                      "Cena lącznie: %s\n\n"
                      "Kaucja: %s\n\n"
                      "Najemca: %s\n"
                      "Nip: %s\n"
                      "Adres: %s, %s\n"
                      "Kod pocztowy: %s\n"
                      "Telefon: %s\n"
                      "E-mail: %s\n"
                      "PESEL: %s\n"
                      "Numer prawa jazdy: %s\n\n"
                      "Numer karty płatniczej: %s\n"
                      "Data ważnośći: %s %s\n"
                      "Kod CVV: %s\n\n"
                      "Uwagi do zamówienia: %s\n\n"
                      "\n\nPlease don't reply to this message. "
                      "For the answer use the e-mail specified by the client."
                      % (pay, reservation_code, car_name, date_start, date_end, rent_days, price_day, limit_day, rent_price, ', \n'.join(selected), extra_services, final_price, actual_deposit, name, nip, street, city, zip, phone, email, pesel, license, card_number, card_month, card_year, card_cvv, remarks),
                      'office@blackcars.pl', recipients)
            send_mail("[BlackCars] Dziękujemy za Rezerwacje",
                      "Dzień dobry,\n\n"
                      "Dziękujemy za dokonanie rezerwacji w wypożyczalni samochodów klasy premium blackcars.pl W tej wiadomości przesyłamy szczegóły Państwa rezerwacji\n\n"
                      "Skontaktujemy się z Państwem wkrótce w celu potwierdzenia rezerwacji.\n\n"
                      "Wybrana metoda płatności: %s\n"
                      "%s \n\n\n"
                      "Numer rezerwacji: %s\n"
                      "Auto: %s\n\n"
                      "Odbiór: %s\n"
                      "Zwrot: %s\n"
                      "Doby: %s\n"
                      "Cena za dobę: %s\n"
                      "Całkowity limit km: %s\n"
                      "Сena za wynajem lącznie: %s\n\n"
                      "Wybrane opcje dodatkowe:\n"
                      "%s\n"
                      "Opcje dodatkowe: %s\n\n"
                      "Cena lącznie: %s\n\n"
                      "Kaucja: %s\n\n"
                      "Najemca: %s\n"
                      "Nip: %s\n"
                      "Adres: %s, %s\n"
                      "Kod pocztowy: %s\n"
                      "Telefon: %s\n"
                      "E-mail: %s\n"
                      "PESEL: %s\n"
                      "Numer prawa jazdy: %s\n\n"
                      "Uwagi do zamówienia: %s\n\n"
                      "Z poważeniem / Best regards\n\n---\n\nblackcars.pl\n\ntel.: +48 720-889-788\ne-mail: office@blackcars.pl\nwww: https://blackcars.pl/\nFacebook: @blackcarspl"
                      % (pay, text_pay, reservation_code, car_name, date_start, date_end, rent_days, price_day, limit_day, rent_price, ', \n'.join(selected), extra_services, final_price, actual_deposit, name, nip, street, city, zip, phone, email, pesel, license, remarks),
                      'office@blackcars.pl', [cc_form.cleaned_data['email']])

        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return redirect('/sukces_reservation')


def car_detail(request, car_slug):
    car = Car.objects.get(slug_car=car_slug)
    rent_periods = CarRentPeriod.objects.filter(car__slug_car=car_slug)
    initial = {'date_start': request.session.get('date_start', 'no date'), 'date_end': request.session.get('date_end', 'no date')}
    form = SmallReservationForm(request.POST or None, initial=initial)
    if request.method == 'POST' and form.is_valid():
        request.session['date_start'] = form.cleaned_data['date_start']
        request.session['date_end'] = form.cleaned_data['date_end']
        return redirect('/' + car_slug + '/rezerwacja')
    return render_tamplate("car_detail.html", {'car': car, 'rent_periods': rent_periods}, request)


def reservation(request, slug_car_reservation):
    car = Car.objects.get(slug_car=slug_car_reservation)
    rent_periods = CarRentPeriod.objects.filter(car__slug_car=slug_car_reservation)
    option_reservation = ExtraOptions.objects.filter(car__slug_car=slug_car_reservation)
    initial = {'payment_method': request.session.get('payment_method', 'no data')}
    if 'date_start' and 'date_end' in request.session:
        date_start = request.session['date_start']
        date_end = request.session['date_end']
        dct = {'car': car,  'rent_periods': rent_periods, 'option_reservation': option_reservation, 'date_start': date_start, 'date_end': date_end}
    else:
        dct = {'car': car, 'rent_periods': rent_periods, 'option_reservation': option_reservation}
    if request.method == 'POST':
        cc_form = ReservationForm(request.POST, initial=initial)
        if cc_form.is_valid():
            request.session['payment_method'] = cc_form.cleaned_data['pay']
            return reservation_form(request)
        else:
            return render_tamplate("reservation.html", dct, request)
    else:
        return render_tamplate("reservation.html", dct, request)


def sukces_reservation(request):
    if 'payment_method' in request.session:
        payment_method = request.session['payment_method']
        dct = {'payment_method': payment_method}
    else:
        dct = {}
    return render_tamplate("sukces_reservation.html", dct, request)


def service(request, service_slug):
    service = Service.objects.get(slug_service=service_slug)
    return render_tamplate("service_detail.html", {'service': service}, request)


def cars_for_weddings(request):
    return render_tamplate("cars_for_weddings.html", {}, request)


def sukces(request):
    return render_tamplate("sukces.html", {}, request)


def privacy_policy(request):
    return render_tamplate("privacy_policy.html", {}, request)


def regulations(request):
    return render_tamplate("regulations.html", {}, request)


def sukcess_newsletter(request):
    return render_tamplate("success_newsleter.html", {}, request)


def success_page(request):
    return render_tamplate("success_page.html", {}, request)


def umowa_najmu(request):
    return render_tamplate("umowa-najmu.html", {}, request)


def regulamin_wypozyczalni(request):
    return render_tamplate("regulamin-wypozyczalni.html", {}, request)


def service_main(request):
    servicepage = ServicePage.objects.all()
    servicetable = ServiceTable.objects.all()
    service = Service.objects.all()
    dct = {'servicepage': servicepage, 'servicetable': servicetable, 'service': service}
    if request.method == 'POST':
        c_form = ContactForm(request.POST)
        if c_form.is_valid():
            return contact_form(request)
        else:
            return render_tamplate("service.html", dct, request)
    else:
        return render_tamplate("service.html", dct, request)


def error404(request, exception):
    template = loader.get_template('404.htm')
    context = Context({
        'message': 'All: %s' % request,
    })
    return HttpResponse(content=template.render(context), content_type='text/html; charset=utf-8', status=404)


def error500(request):
    template = loader.get_template('500.htm')
    context = Context({
        'message': 'All: %s' % request,
    })
    return HttpResponse(content=template.render(context), content_type='text/html; charset=utf-8', status=500)

@require_GET
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
