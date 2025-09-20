from django.db import models

from bases.model import BaseModel
from bases.paths import user_profile_image_directory_path, passport_upload_path

class User(BaseModel):
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=32)
    telegram_chat_id = models.IntegerField(unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=32, null=True, blank=True)
    phone_number = models.CharField(max_length=13, unique=True)
    
    passport_front = models.FileField(upload_to=passport_upload_path, null=True, blank=True)
    passport_back = models.FileField(upload_to=passport_upload_path, null=True,blank=True)

    is_block = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    profile_image = models.ImageField(upload_to=user_profile_image_directory_path, default="default/profile_image.png")

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"
    def __str__(self):
        return self.username