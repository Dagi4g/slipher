from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

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
    
class WatchHistory(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #the time when the user watched the video.
    #this is used to keep track of the last time the user watched the video.
    watched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('video', 'user')  # Ensure a user can only have one entry per video

    def __str__(self):
        return f"{self.user} watched {self.video.title} at {self.watched_at}"

class Feedback(models.Model):
    feedback_type = [("very helpful","Very Helpful"),
                ('helpful','Helpful'),
                ('average','Average'),
                ('very poor','Very Poor'),
                ('not helpful','Not Helpful')
                ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=12, choices=feedback_type, default='good')
    class Meta:
        unique_together = ('video', 'user')




