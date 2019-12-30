# Generated by Django 2.2.7 on 2019-12-22 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turntable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('prize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turntable.Prizes')),
            ],
        ),
    ]