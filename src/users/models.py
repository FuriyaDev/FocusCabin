from django.db import models

from bases.model import BaseModel
from bases.paths import user_profile_image_directory_path

class User(BaseModel):
    username = models.CharField(max_length=64, uniqe=True)
    password = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=32, null=True, blank=True)
    phone_number = models.CharField(max_length=13, uniqe=True)

    is_block = models.BooleanField(default=False)

    profile_image = models.ImageField(upload_to=user_profile_image_directory_path, default="default/profile_image.png")



