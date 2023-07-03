from django.db import models

# Create your models here.
class BlogTopic(models.Model):
    """A blog tile that displays an image, title, and short entry."""
    title = models.TextField(max_length=50)
    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
    
class BlogEntry(models.Model):
    """The entry of a specific blog topic."""
    topic = models.ForeignKey(BlogTopic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Return a simple string representing the entry."""
        return f"{self.text[:50]}..."
