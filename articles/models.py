from django.db import models

# Create your models here.

class Review(models.Model): # models에서 모델을 가져온다
    title = models.CharField(max_length=20) # 제한이 있을 때
    content = models.TextField() # 제한이 없을 때
    movie_name = models.TextField()
    grade = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
