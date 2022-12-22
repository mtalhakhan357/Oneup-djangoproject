from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from games.models import *
from app_s.models import *
# Create your models here.
class contactrequests(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100,)
    user_email = models.CharField(max_length=150,)
    user_subject = models.CharField(max_length=200,)
    user_type = models.CharField(max_length=100,)
    user_message = models.TextField()


class statustics(models.Model):
    page_id = models.AutoField(primary_key=True)
    page_name = models.CharField(max_length=100,)
    page_href = models.CharField(max_length=150,)
    page_type = models.CharField(max_length=100,)
    page_views = models.IntegerField(default=0)
    
class page_details(models.Model):
    page_id = models.AutoField(primary_key=True)
    page_name = models.CharField(max_length=120)
    page_tittle = models.TextField(default=''' " Download name version (Android) - oneup.com " .this tittle will be shown on google search.''')
    page_description = models.TextField(default=''' Download name version for Android for free , without viruses ... .this will be shown in two line tittle in gooogle search  ''')
    page_keywords = models.TextField(default='keywords are like tags in YT or whatever . this will be use in google search engin search the pages ex - oneup , name , download name , download name for android , name for android for free ')
    og_tittle = models.TextField(default=''' "name(subcategory) - oneup.com " .this tittle will be shown when the url will be share on whatsapp or instagram''')
    og_description = models.TextField(default='this description will be shown when the url will be share on whatsapp or instagram .max = 20 wrods')
    og_image =  models.ImageField(upload_to='main/icon/og') 
    


class despAndText(models.Model):
    text_id = models.AutoField(primary_key=True)
    text_name = models.CharField(max_length=120)
    text_tittle = models.CharField(max_length=120)
    text_body = models.TextField(default="about theat page in the html page but dont make more some have been already made")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='main/user',default='default-avatar.png')
    def __str__(self):
        return f'{self.user.username} Profile'

# class banners(models.Model);
#     sno = models.AutoField(primary_key=True)
#     page_name = models.CharField(max_length=120)
#     title_1 = models.CharField(max_length=200)
#     img_1 = models.ImageField(upload_to='main/banners/img')
#     desc_1 =
#     href_1 = 
