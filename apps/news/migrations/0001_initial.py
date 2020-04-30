# Generated by Django 3.0.5 on 2020-04-30 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('is_publish', models.BooleanField(default=False)),
                ('published_at', models.DateField(auto_now_add=True)),
                ('categories', models.ManyToManyField(related_name='news', to='news.NewsCategory')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
