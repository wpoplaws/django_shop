from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Camping(models.Model):
    VOIVODESHIP_CHOICES = (
        ('dolnośląskie', 'dolnośląskie'), ('kujawsko-pomorskie', "kujawsko-pomorskie"),
        ('lubelskie', 'lubelskie'), ('lubuskie', "lubuskie"),
        ('łódzkie', 'łódzkie'), ('małopolskie', "małopolskie"),
        ('mazowieckie', 'mazowieckie'), ('opolskie', "opolskie"),
        ('podkarpackie', 'podkarpackie'), ('podlaskie', "podlaskie"),
        ('pomorskie', 'pomorskie'), ('śląskie', "śląskie"),
        ('świętokrzyskie', 'świętokrzyskie'), ('warmińsko-mazurskie', "warmińsko-mazurskie"),
        ('wielkopolskie', 'wielkopolskie'), ('zachodniopomorskie', "zachodniopomorskie"),
    )

    name = models.CharField(max_length=128, blank=True, )
    slug = models.SlugField(max_length=40, blank=True)
    image = models.ImageField(upload_to="Images", blank=True, )
    city = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=6, blank=True)
    address = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=128, blank=True, )
    email = models.EmailField(default="", blank=True, )
    phone_number = models.CharField(max_length=12, blank=True, )
    voivodeship = models.CharField(max_length=30, choices=VOIVODESHIP_CHOICES, default='draft')
    latitude = models.FloatField(blank=True, max_length=30)
    longitude = models.FloatField(blank=True, max_length=30)
    price_list = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Camping, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('camping_detail',
                       args=[self.slug])

