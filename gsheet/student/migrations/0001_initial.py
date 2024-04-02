# Generated by Django 4.1.13 on 2024-04-01 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('age', models.CharField(max_length=127)),
                ('address', models.CharField(blank=True, default=None, max_length=127, null=True)),
            ],
        ),
    ]
