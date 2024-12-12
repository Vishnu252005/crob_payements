from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)  
    email = models.EmailField(max_length=255, blank=True, null=True)  
    profile_pic = models.ImageField(upload_to="profile_pics/", null=True, blank=True)
    phone_num = models.CharField(max_length=15, blank=True, null=True) 
    college_name = models.CharField(max_length=255, blank=True, null=True)
    branch = models.CharField(max_length=255, blank=True, null=True)
    

    YEAR_CHOICES = [
        (1, 'First Year'),
        (2, 'Second Year'),
        (3, 'Third Year'),
        (4, 'Fourth Year'),
    ]
    year = models.IntegerField(choices=YEAR_CHOICES, default=1)

    def __str__(self):
        return f"{self.user.username}'s Profile"
