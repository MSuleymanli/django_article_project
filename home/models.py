from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    author=models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    content=RichTextField()
    creadet_date=models.DateTimeField(auto_now_add=True)
    image=models.FileField(upload_to="Article Image",blank=True,null=True,verbose_name="Photo")

    def __str__(self):
        return self.title


    
class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE,related_name="comment")
    comment_author=models.CharField(max_length=50)
    comment_content=models.TextField(max_length=200)
    comment_date=models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return self.comment_author