from django.contrib.auth import get_user_model
from users.models import CustomUser
from django.db import models
from django.urls import reverse




CAT_CHOICES = (  #CATEGORY
        ('политика', 'Политика'),
        ('общество', 'Общество'),
        ('чп', 'ЧП'),
        ('экономика', 'Экономика'),
        ('дополнительно', 'Дополнительно'),
    )





class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CAT_CHOICES, default='дополнительно')
    image = models.ImageField(default=None, null=True)
    author = models.ForeignKey(
    CustomUser,
    on_delete=models.CASCADE,
    related_name='articles')




    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])




class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments',)
    body = models.CharField(max_length=100)
    author = models.ForeignKey(
                                get_user_model(),
                                on_delete=models.CASCADE,
                            )



    def __str__(self):
        return self.body


    def get_absolute_url(self):
        return reverse('article_list')