# Generated by Django 2.0.6 on 2018-06-15 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulos',
            old_name='creado',
            new_name='autor',
        ),
        migrations.AddField(
            model_name='articulos',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]