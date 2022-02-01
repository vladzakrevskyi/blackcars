from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from website.views import robots_txt
from django.contrib import admin
from . import views

urlpatterns = [
    # robots.txt
    path('robots.txt', robots_txt),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    re_path(r'^nasza-flota/?$', views.our_cars, name='our-cars'),
    re_path(r'^kontakt/?$', views.contact, name='contact'),
    re_path(r'^uslugi/?$', views.service_main, name='service_main'),
    re_path(r'^auto-do-slubu/?$', views.cars_for_weddings, name='cars_for_weddings'),
    re_path(r'^polityka-prywatnosci/?$', views.privacy_policy, name='privacy_policy'),
    re_path(r'^regulamin/?$', views.regulations, name='regulations'),
    re_path(r'^sukces_reservation/?$', views.sukces_reservation, name='sukces_reservation'),
    re_path(r'^umowa-najmu/?$', views.umowa_najmu, name='umowa-najmu'),
    re_path(r'^regulamin-wypozyczalni/?$', views.regulamin_wypozyczalni, name='regulamin-wypozyczalni'),
    re_path(r'^sukcess_newsletter/?$', views.sukcess_newsletter, name='sukccess_newsletter'),
    re_path(r'^success_page/?$', views.success_page, name='success_page'),
    re_path(r'^blog/?$', views.blog, name='blog'),
    re_path(r'^blog/(?P<post_slug>[^/]+)/?$', views.blog_detail, name='blog_post'),
    re_path(r'^(?P<slug_car_reservation>[^/]+)/rezerwacja/?$', views.reservation, name='car-reservation'),
    re_path(r'^(?P<car_slug>[^/]+)/?$', views.car_detail, name='car-detail'),
    path('summernote', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.error404
handler500 = views.error500


