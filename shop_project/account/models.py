from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.db.models.signals import post_save


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset() \
            .filter(status='published')


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    slug = models.SlugField(default='SOME STRING')
    friends = models.ManyToManyField("Profile", blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "{}".format(self.slug)

    def get_slug(self):
        '''
        Returns the short name for the user.
        '''
        return self.slug

    def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
        if created:
            try:
                Profile.objects.create(user=instance)
            except:
                pass

    post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)


class FriendRequest(models.Model):
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='to_user')
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='from_user')
    timestamp = models.DateTimeField(auto_now_add=True)  # set when created

    def __str__(self):
        return "From {}, to {}".format(self.from_user.username, self.to_user.username)


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
        ('nie_wybrano', 'nie wybrano')
    )

    STATUS_CHOICES = (
        ('draft', 'Draft'), ('published', "Published"),
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
    voivodeship = models.CharField(max_length=30, choices=VOIVODESHIP_CHOICES, default='nie_wybrano')
    latitude = models.FloatField(blank=True, max_length=30)
    longitude = models.FloatField(blank=True, max_length=30)
    price_list = models.CharField(max_length=1000)
    description = models.TextField(max_length=5000, default="", blank=True)
    published = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Camping, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('camping_detail',
                       args=[self.slug])
