from django.db import models

class Article(models.Model):
    author=models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    content=models.TextField()
    creadet_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


    