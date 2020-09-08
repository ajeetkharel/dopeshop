# Generated by Django 3.0.3 on 2020-09-06 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='category',
            new_name='subcategory',
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='default_item.jpg', upload_to='item_images'),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
