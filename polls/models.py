from django.db import models

# Create your models here.


class Categories(models.Model):
    Name = models.CharField(max_length=20,primary_key=True)
    Photo = models.CharField(max_length=25)


class User(models.Model):
    Id = models.CharField(max_length=30,primary_key=True)
    Name = models.CharField(max_length=20)
    Photo = models.CharField(max_length=25)

class Post(models.Model):

    Id = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE)
    Header_photo = models.CharField(max_length=25)
    Writer = models.ForeignKey(User, on_delete=models.CASCADE)
    Create_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    Summary = models.TextField()



class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    class Meta:
        unique_together = (("user", "post"),)

class Mark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    class Meta:
        unique_together = (("user", "post"),)

class ReadsPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    class Meta:
        unique_together = (("user", "post"),)

class Content(models.Model):
    Id = models.ForeignKey(Post, on_delete=models.CASCADE, primary_key=True)
    Content1 = models.CharField(max_length=30)
    Content2 = models.CharField(max_length=20)
    Main_content = models.TextField()

class File2(models.Model):
    file = models.FileField(blank=False, null=False)
#name='%m-%d-%y-%H:%M:%S.%f',