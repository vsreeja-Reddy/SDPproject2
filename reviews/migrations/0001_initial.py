# Generated by Django 5.0 on 2024-02-20 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TouristReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('rating', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/media/review_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
