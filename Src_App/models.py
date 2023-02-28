from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



################################################################################

class Profile(models.Model):

    user = models.ForeignKey(User , on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='profile_images' , default='example.png' )
    cover_img = models.ImageField(upload_to='profile_images' , default='example.png' )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_info = models.CharField(max_length=50 , null=True)
    bios = models.TextField()
    followers = models.ManyToManyField(User , related_name='followers')
    following = models.ManyToManyField(User , related_name='following')
    
    def __str__(self):

        return (f"{self.first_name} {self.last_name}")



#################################################################################

class Post(models.Model):

    user = models.ForeignKey(User , on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile , on_delete=models.CASCADE , null=True , )
    img = models.ImageField(upload_to='posts_images' , default='example.png')
    likers = models.ManyToManyField(User , related_name='Likers')
    likes = models.IntegerField(default=0)

    def __str__(self):

        return (f"{self.id}")



##################################################################################

class Comment(models.Model):

    user = models.ForeignKey(User , on_delete=models.CASCADE)
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile , on_delete=models.CASCADE , null=True)
    text = models.TextField()


##################################################################################

class Notification(models.Model):

    sender = models.ForeignKey(User , on_delete=models.CASCADE , related_name='sender')
    sender_profile = models.ForeignKey(User , on_delete=models.CASCADE , related_name='sender_profile')
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='post')
    reciever = models.ForeignKey(User , on_delete=models.CASCADE , related_name='reciever')
    reciever_profile = models.ForeignKey(Profile , on_delete=models.CASCADE , related_name='reciever_profile')




