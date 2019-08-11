from django.db import models

# Create your models here.


class Cover(models.Model):
    cover_image = models.ImageField(null=True, blank=True)


class Tiles(models.Model):

    heading = models.CharField(max_length=255, null=True, blank=True)

    image1 = models.ImageField(null=True, blank=True)
    image1_heading = models.CharField(max_length=255)
    image1_para = models.TextField(default="")

    image2 = models.ImageField(null=True, blank=True)
    image2_heading = models.CharField(max_length=255)
    image2_para = models.TextField(default="")

    image3 = models.ImageField(null=True, blank=True)
    image3_heading = models.CharField(max_length=255)
    image3_para = models.TextField(default="")

    image4 = models.ImageField(null=True, blank=True)
    image4_heading = models.CharField(max_length=255)
    image4_para = models.TextField(default="")

    image5 = models.ImageField(null=True, blank=True)
    image5_heading = models.CharField(max_length=255)
    image5_para = models.TextField(default="")

    image6 = models.ImageField(null=True, blank=True)
    image6_heading = models.CharField(max_length=255)
    image6_para = models.TextField(default="")

    def __str__(self):
        return self.heading[:50]


class Section2(models.Model):

    sec2_heading = models.CharField(max_length=255)
    sec2_image1 = models.ImageField(null=True, blank=True)
    sec2_image2 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.sec2_heading[:50]


class Videos(models.Model):

    video1 = models.TextField(default="Video not available")
    video1_heading = models.CharField(max_length=255)
    video1_para = models.TextField()

    video2 = models.TextField(default="Video not available")
    video2_heading = models.CharField(max_length=255)
    video2_para = models.TextField()

    video3 = models.TextField(default="Video not available")
    video3_heading = models.CharField(max_length=255)
    video3_para = models.TextField()


class About(models.Model):

    profile_picture = models.ImageField(null=True, blank=True)
    profile_para = models.TextField(default="Fill it out")

    my_map = models.TextField(default="map not available")
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    facebook = models.TextField(default="facebook.com")
    youtube = models.TextField(default="youtube.com")