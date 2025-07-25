from django.db import models

class Video(models.Model):
    video_id = models.CharField(max_length=20,unique=True)
    title = models.CharField(max_length=200)
    channel_name = models.CharField(max_length=200)
    video_len = models.CharField(max_length=10)
    language = models.CharField(max_length=10,default="en")
    #the tag might be usefull to to catagorize videos in the future.
    tag = models.CharField(blank=True,null=True)

    def __str__(self):
        return self.title





