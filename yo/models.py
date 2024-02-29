from django.db import models


# Create your models here.

class Human(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    name = models.CharField(null=False, blank=False, unique=True, max_length=50, verbose_name="name")
    age = models.PositiveIntegerField(null=False, blank=False, unique=False)
    image = models.ImageField(null=False, blank=False, upload_to='images/', default="def.jpg")
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=False, blank=False)
    mobile = models.PositiveIntegerField(null=False, blank=False, unique=False)
    email = models.EmailField(null=False, blank=False)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def __str__(self):
        return self.name
