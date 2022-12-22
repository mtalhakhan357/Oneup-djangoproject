from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.validators import MaxValueValidator , MinValueValidator
# Create your models here.
class game(models.Model):
    gameid = models.AutoField
    game_id = models.CharField(max_length=15,default='00001')
    game_name = models.CharField(max_length=50)
    game_author = models.CharField(max_length=150)
    game_author_href = models.CharField(max_length=1000,default='link to go to official web of copyrighter')
    game_categary = models.CharField(max_length=100,default='Action Action-Adventure Adventure Simulation Stratergy Sports Puzzle Arcade Casual Shooting Emulators Cards ')
    game_sub_categary = models.CharField(max_length=100,default='Windows MAC Android')
    game_description = models.CharField(max_length=37)
    game_maindescription = models.TextField()
    game_version = models.CharField(max_length=30)
    game_license = models.CharField(max_length=100,default='Free')
    game_size = models.CharField(max_length=50,default='000 MB')
    game_pack_name = models.CharField(max_length=50,default='cao.zip')
    game_download_href = models.CharField(max_length=1000,default='/')
    game_release_date = models.DateField()
    game_publish_date = models.DateField()
    views = models.IntegerField(default=0,null=True,blank=True)
    game_image = models.ImageField(upload_to='download/game/img')
    ratting = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )#
    game_tags = models.TextField(default='''"Download (name) for Android for free, without any viruses, from one up , Try the latest version of (name) for Android , name , category , subcategory , etc "''')
    page_description = models.TextField(default="above 40 words , bellow 60 Words Download (name) for Android for free, without any viruses, from one up , Try the latest version of (name) for Android . end must contain ...")
    def __str__(self):
        return self.game_name

class gamecomments(models.Model):
    sno = models.AutoField(primary_key=True)#
    user = models.ForeignKey(User,on_delete=models.CASCADE)#
    game = models.ForeignKey(game,on_delete=models.CASCADE)#
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)#
    comment = models.TextField()#
    ratting = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )#
    like = models.IntegerField(default=0)#
    timestamp =  models.DateTimeField(default=now)