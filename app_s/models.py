from django.db import models
from django.forms import ModelForm, Form
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator , MinValueValidator
from django.forms import DateField, CharField, ChoiceField, TextInput
from django.utils.timezone import now

# Create your models here.
class app (models.Model):
    appid = models.AutoField
    app_id = models.CharField(max_length=15,default='00001')
    app_name = models.CharField(max_length=50)
    app_author = models.CharField(max_length=150)
    app_author_href = models.CharField(max_length=1000,default='/')
    app_categary = models.CharField(max_length=100,default='Social Communication Business Educational Lifestyle Entertainment Travel Utility Tools Multimedia Business Animation 3D-Modeling Development')
    app_sub_categary = models.CharField(max_length=100,default='Windows Android')
    app_description = models.CharField(max_length=37)
    app_maindescription = models.TextField()
    app_version = models.CharField(max_length=30)
    app_license = models.CharField(max_length=100,default='Free')
    app_size = models.CharField(max_length=50,default='000 MB')
    app_pack_name = models.CharField(max_length=50,default='cao.zip')
    app_download_href = models.CharField(max_length=1000,default='/')
    app_release_date = models.DateField()
    app_publish_date = models.DateField()
    views = models.IntegerField(default = 0,null = True,blank = True)
    ratting = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )#
    app_image = models.ImageField(upload_to='download/app/img')
    app_tags = models.TextField(default='''"Download (name) for Android for free, without any viruses, from one up , Try the latest version of (name) for Android , name , category , subcategory , etc "''')
    page_description = models.TextField(default="Above 50 Words")
    def __str__(self):
        return self.app_name

class appcomments(models.Model):
    sno = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    app = models.ForeignKey(app,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    comment = models.TextField()
    ratting = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )#
    like = models.IntegerField(default=0)#
    timestamp =  models.DateTimeField(default=now)