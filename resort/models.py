from turtle import position
from django.db import models
from datetime import date
from email import message
from email.mime import image
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Hero(models.Model):

    class Meta:
        verbose_name_plural = 'Hero Section'
        verbose_name = 'Hero Section'

    name = models.CharField(max_length=100, blank=True, null=True, default='RESORT NAME', verbose_name='Set a Cool Name of ReSort')
    tag = models.CharField(max_length=100, blank=True, null=True, default='STAY WITH FRIENDS & FAMILIES', verbose_name='Set a Tagline for Hero Section')
    greet = models.CharField(max_length=100, blank=True, null=True, default='GET ACCOMMODATION TODAY', verbose_name='Set a Greeting for Hero Section')
    class_name = models.CharField(max_length=25, blank=True, null=True, default='Ex: w3layouts-banner-top1 or w3layouts-banner-top2 or null', verbose_name='Set One of these Class Name')      
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.name} {self.tag}'




class ServiceChart(models.Model):

    class Meta:
        verbose_name_plural = 'Service Chart'
        verbose_name = 'Service Chart'

    name = models.CharField(max_length=50, blank=True, null=True, default='MASTER BEDROOM', verbose_name='Set a Name for Service')
    company_name = models.CharField(max_length=50, blank=True, null=True, default='RESORT PALACE', verbose_name='Set a Company Name')
    icon = models.CharField(max_length=20, blank=True, null=True, default='w3_road', verbose_name='Set a Icon Class Name')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} {self.company_name}'


class About(models.Model):

    class Meta:
        verbose_name_plural = 'About Section'
        verbose_name = 'About Section'

    image_one = models.ImageField(blank=True, null=True, upload_to='About_Images/', verbose_name='Upload Image for About Section')
    image_two = models.ImageField(blank=True, null=True, upload_to='About_Images/', verbose_name='Upload Image for About Section')
    heading = models.CharField(max_length=100, blank=True, null=True, default='About Our Resort Palace', verbose_name='Set a Heading')
    description = models.CharField(max_length=100, blank=True, null=True, default='Short Description', verbose_name='Set a Description')
    offer = models.CharField(max_length=100, blank=True, null=True, default="You'll love all the amenities we offer!", verbose_name='Set a Offer')
    offer_description = models.CharField(max_length=100, blank=True, null=True, default='Offer Short Description', verbose_name='Set a Offer Description')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.heading} {self.description}'

    @property
    def image_oneURL(self):
        try:
            url = self.image_one.url
        except:
            url = ''
        return url

    @property
    def image_twoURL(self):
        try:
            url = self.image_two.url
        except:
            url = ''
        return url


class Services(models.Model):

    class Meta:
        verbose_name_plural = 'Services Section'
        verbose_name = 'Services Section'

    heading = models.CharField(max_length=50, blank=True, null=True, default='Ex: Stay First, Pay After or 24 Hours Restaurant', verbose_name='Set a Heading')
    description = models.CharField(max_length=100, blank=True, null=True, default='Short Description', verbose_name='Set a Description')
    check_point_one = models.CharField(max_length=30, blank=True, null=True, default='Check Point One', verbose_name='Set a Bullet Point')
    check_point_two = models.CharField(max_length=30, blank=True, null=True, default='Check Point Two', verbose_name='Set a Bullet Point')
    icon_class = models.CharField(max_length=20, blank=True, null=True, default='Ex: fa-clock-o or fa-credit-card', verbose_name='Set a Icon Class Name')
    position_class = models.CharField(max_length=20, blank=True, null=True, default='Ex: left or right', verbose_name='Set a Position Class Name')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.heading} {self.description}'



class Team(models.Model):

    class Meta:
        verbose_name_plural = 'Team Section'
        verbose_name = 'Team Section'


    name = models.CharField(max_length=50, blank=True, null=True, default='Ex: John Doe', verbose_name='Set a Name')
    designation = models.CharField(max_length=50, blank=True, null=True, default='Ex: CEO', verbose_name='Set a Designation')
    short_intro = models.CharField(max_length=100, blank=True, null=True, default='Short Description', verbose_name='Set a Short Intro')
    facebook_link = models.CharField(max_length=100, blank=True, null=True, default='https://www.facebook.com/', verbose_name='Set your Facebook Link')
    twitter_link = models.CharField(max_length=100, blank=True, null=True, default='https://www.twitter.com/', verbose_name='Set your Twitter Link')
    google_plus_link = models.CharField(max_length=100, blank=True, null=True, default='https://www.google.com/', verbose_name='Set your Google Plus Link')
    rss_link = models.CharField(max_length=100, blank=True, null=True, default='https://www.rss.com/', verbose_name='Set your Rss Link')
    tab_name = models.CharField(max_length=100, blank=True, null=True, default='Ex: tab1', verbose_name='Set a Tab Name')
    image = models.ImageField(blank=True, null=True, upload_to='Team_Images/', verbose_name='Upload Image for Team Section')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} {self.designation}'

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Gallery(models.Model):

    class Meta:
        verbose_name_plural = 'Gallery Section'
        verbose_name = 'Gallery Section'

    image = models.ImageField(blank=True, null=True, upload_to='Gallery_Images/', verbose_name='Upload Image for Gallery Section')
    image_tag = models.CharField(max_length=50, blank=True, null=True, default='Ex: Resort Palace', verbose_name='Set a Image Tag')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.image_tag}'

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class RoomsRates(models.Model):

    class Meta:
        verbose_name_plural = 'Rooms Rates Section'
        verbose_name = 'Rooms Rates Section'

    name = models.CharField(max_length=50, blank=True, null=True, default='Ex: Deluxe Room', verbose_name='Set a Room Name')
    price = models.CharField(max_length=50, blank=True, null=True, default='Ex: $300', verbose_name='Set a Room Price')   
    image = models.ImageField(blank=True, null=True, upload_to='Rooms_Images/', verbose_name='Upload Image for Rooms Section')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} {self.price}'

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Visitors(models.Model):

    class Meta:
        verbose_name_plural = 'Visitors Review Section'
        verbose_name = 'Visitor Review Section'

    image_one = models.ImageField(blank=True, null=True, upload_to='Visitors_Images/', verbose_name='Upload Back Image for Visitors Section')
    image_two = models.ImageField(blank=True, null=True, upload_to='Visitors_Images/', verbose_name='Upload Front Image for Visitors Section')
    title = models.CharField(max_length=50, blank=True, null=True, default='Ex: Best Resort', verbose_name='Set a Title')
    description = models.CharField(max_length=100, blank=True, null=True, default='Short Description', verbose_name='Set a Description')
    name = models.CharField(max_length=50, blank=True, null=True, default='Ex: John Doe', verbose_name='Set a Name')
    location = models.CharField(max_length=50, blank=True, null=True, default='Ex: California', verbose_name='Set a Location')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} {self.description}'

    @property
    def image_oneURL(self):
        try:
            url = self.image_one.url
        except:
            url = ''
        return url

    @property
    def image_twoURL(self):
        try:
            url = self.image_two.url
        except:
            url = ''
        return url


class saveContact(models.Model):

    class Meta:
        verbose_name_plural = 'Save Contact From User'
        verbose_name = 'Save Contact From User'

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)



class saveChecking(models.Model):
    
        class Meta:
            verbose_name_plural = 'Save Checking info From User'
            verbose_name = 'Save Checking info From User'
    
        roomtype = models.CharField(max_length=50)
        adate = models.CharField(max_length=50)
        ddate = models.CharField(max_length=50)
        


class bookingList(models.Model):
    
    class Meta:
        verbose_name_plural = 'Set Booking List'
        verbose_name = 'Set Booking List'

        db_table = "booking_list"
    
    room_type = models.CharField(max_length=50)
    check_in = models.CharField(max_length=50)
    check_out = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)


class searchBooking(models.Model):
        
    room_type = models.CharField(max_length=50)
    check_in = models.CharField(max_length=50)
    check_out = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)


class booking(models.Model):

    class Meta:
        verbose_name_plural = 'Get Booking Lists'
        verbose_name = 'Get Booking List'


    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    check_in = models.CharField(max_length=50)
    check_out = models.CharField(max_length=50)
    room_price = models.CharField(max_length=50)



    def __str__(self):
        return f'{self.name} {self.email} {self.number} {self.check_in} {self.check_out} {self.room_price}'
