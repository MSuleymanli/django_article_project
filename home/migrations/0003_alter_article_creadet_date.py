# Generated by Django 5.0.6 on 2024-06-03 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_article_image_alter_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='creadet_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
