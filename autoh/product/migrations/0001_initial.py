# Generated by Django 4.0.4 on 2022-08-25 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=100)),
                ('b_img', models.ImageField(upload_to='pic')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
