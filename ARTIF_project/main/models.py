from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    # start_title = models.CharField(max_length = 200)
    # start_content = models.TextField()
    # start_published = models.DateTimeField("date published")

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    # email = models.EmailField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        # return self.start_title
        return self.user.username