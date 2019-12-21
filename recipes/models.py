from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Recipe(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)   
    content = RichTextField()       
    created_date = models.DateTimeField(auto_now_add=True)
    recipe_image = models.FileField(blank = True , null = True , verbose_name = "Please,Add an image...")
    def __str__(self):  
        return self.title

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,verbose_name = "Recipe",related_name="comments")
    comment_author = models.CharField(max_length = 50, verbose_name = "name")
    comment_content = models.CharField(max_length = 200, verbose_name = "comment")
    comment_date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.comment_content



    
