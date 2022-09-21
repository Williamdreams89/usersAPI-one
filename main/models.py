from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from main.managers import StudentManager


class Student(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=14, unique=True)
    programme = models.CharField(help_text="Programme of study", max_length=120)
    # profile_pic = models.ImageField()
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'student_id','programme']


    objects = StudentManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name_}"

