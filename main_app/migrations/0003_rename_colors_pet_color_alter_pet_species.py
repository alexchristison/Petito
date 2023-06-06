# Generated by Django 4.2.1 on 2023-06-06 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_pet_image_pet_colors_pet_species'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='colors',
            new_name='color',
        ),
        migrations.AlterField(
            model_name='pet',
            name='species',
            field=models.CharField(choices=[('a', 'Unicorn'), ('b', 'Bear'), ('c', 'Cat'), ('d', 'Dinosaur')], default='a', max_length=1),
        ),
    ]