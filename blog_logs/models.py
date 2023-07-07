from django.db import models

# Create your models here.
class Post(models.Model):
    """A blog title that displays an image, title, and short entry."""
    title = models.CharField(max_length=150)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}"
