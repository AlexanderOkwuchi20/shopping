# Generated by Django 4.1.7 on 2023-04-18 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_shopcart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('amount', models.CharField(max_length=50)),
                ('paid', models.BooleanField()),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(default='', max_length=200)),
                ('shop_code', models.CharField(max_length=50)),
                ('pay_code', models.CharField(max_length=50)),
                ('pay_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
