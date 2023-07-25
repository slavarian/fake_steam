# Generated by Django 4.2.3 on 2023-07-25 14:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_rename_imgor_game_main_imgor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitecard',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 24, 20, 4, 26, 48724), verbose_name='дата истечения'),
        ),
        migrations.CreateModel(
            name='AdditionalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='games/additional_images/', verbose_name='дополнительное изображение')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_images', to='games.game')),
            ],
            options={
                'verbose_name': 'дополнительное изображение',
                'verbose_name_plural': 'дополнительные изображения',
            },
        ),
    ]
