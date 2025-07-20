from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="blogs"
    )
    body = models.TextField()
    create_date = models.DateField(null=False, auto_now=True)

    def __str__(self) -> str:
        return self.title
