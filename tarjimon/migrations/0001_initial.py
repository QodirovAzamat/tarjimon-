# Generated by Django 5.0 on 2023-12-14 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lugat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inglizcha', models.CharField(max_length=128, verbose_name='Ingilizch')),
                ('uzbekcha', models.CharField(max_length=128, verbose_name='O`zbekcha')),
            ],
        ),
    ]