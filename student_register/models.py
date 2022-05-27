from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=50, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=154, unique=True, blank=True, null=True)

    GENDER =(
        ("Female", "Female"),
        ("Male", "Male"),
        ("Other", "Other"),
        ("Prefer Not Say", "Prefer Not Say"),
    )
    gender = models.CharField(max_length=50, choices=GENDER)

    PATH =(
        ("Aws-Dewops", "Aws-Dewops"),
        ("Data Science", "Data Science"),
        ("Full Stack", "Full Stack"),
        ("Cyber Security", "Cyber Security"),
    )
    path = models.CharField(max_length=50, choices=PATH)


    def __str__(self):
        return f"{self.full_name} {self.path}"