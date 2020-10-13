from rest_framework import serializers
from .models import Article, CAT_CHOICES


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.ChoiceField(choices=CAT_CHOICES, default='дополнительно')

    class Meta:
        model = Article
        fields = ['id', 'category']