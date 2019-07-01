from django.db import models

# Create your models here.
class artif_start(models.Model):
    start_title = models.CharField(max_length = 200)
    start_content = models.TextField()
    start_published = models.DateTimeField("date published")

    def __str__(self):
        return self.start_title