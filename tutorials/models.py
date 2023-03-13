from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tutorial(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    url = models.URLField(
        unique=True, error_messages={"unique": "Tutorial has already been shared!"}
    )
    owner = models.ForeignKey(User, related_name="tutorials", on_delete=models.CASCADE)

    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return self.title
