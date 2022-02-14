from django.db import models

# Create your models here.


class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=10000)
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return str(self.post_id) + ". " + self.title
