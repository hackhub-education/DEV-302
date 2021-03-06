# Generated by Django 2.2.7 on 2020-01-12 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('discount', models.IntegerField()),
                ('value', models.FloatField()),
                ('modified_by', models.CharField(max_length=100)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('state', models.CharField(choices=[('new', 1), ('used', 0)], default='new', max_length=50)),
            ],
        ),
    ]
