from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()



class Song(models.Model):
  
   name = models.CharField(max_length=64)
   url = models.CharField(max_length=150)
   user = models.ForeignKey(User, blank=True, null=True, related_name="song")
   youtube_url = models.CharField(max_length=150,null=True)

   def set_song(self,name,url,youtube_url):
        self.name = name
        self.url = url
        self.youtube_url = youtube_url
        self.save()
        
   def __str__(self):
     return self.name



 #class PlayList(models.Model):

 #   name = models.CharField(max_length=64)

 #   def __str__(self):
  #    return self.name