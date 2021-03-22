# Generated by Django 3.1.7 on 2021-03-21 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
