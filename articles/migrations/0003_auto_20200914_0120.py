# Generated by Django 3.1 on 2020-09-13 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('политика', 'Политика'), ('общество', 'Общество'), ('чп', 'ЧП'), ('экономика', 'Экономика'), ('дополнительно', 'Дополнительно')], default='дополнительно', max_length=20),
        ),
    ]