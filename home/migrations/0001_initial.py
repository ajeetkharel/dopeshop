# Generated by Django 3.0.3 on 2020-09-08 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('usage', models.CharField(choices=[('N', 'New'), ('U', 'Used')], max_length=1)),
                ('condition', models.CharField(blank=True, max_length=255)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(default='default_item.jpg', upload_to='item_images')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Category', verbose_name='Category')),
            ],
        ),
    ]
