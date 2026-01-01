from django.db import models

# Create your models here.


class CustomUser(models.Model):

    # id = models.AutoField(primary_key=True)  # django creates id automatically

    username = models.CharField(
        max_length=50,
        unique=True,
    )

    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    email = models.EmailField(unique=True)

    age = models.IntegerField(null=True, blank=True)
    # optional field blank -> empty input , null value in db

    status = models.CharField(
        max_length=20,
        default="active",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["-created_at"]  # descending order
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "app_users"


# __method_name__() => dunder methods -> it automatically called by python
# __str__ => when obj is converted to string
