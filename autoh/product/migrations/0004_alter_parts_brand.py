# Generated by Django 4.0.4 on 2022-08-25 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_parts_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parts',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='partss', to='product.brands'),
        ),
    ]
