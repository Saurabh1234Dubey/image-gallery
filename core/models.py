from django.db import models

# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(Base):
    """
    This model is used for Image Category.
    """
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class Media(Base):
    """
    This model is used for Image collection.
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='media')
    title = models.CharField(max_length=250, null=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.category.name
