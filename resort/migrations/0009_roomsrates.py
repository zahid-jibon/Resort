# Generated by Django 4.0.3 on 2022-03-08 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resort', '0008_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomsRates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Ex: Deluxe Room', max_length=50, null=True, verbose_name='Set a Room Name')),
                ('price', models.CharField(blank=True, default='Ex: $300', max_length=50, null=True, verbose_name='Set a Room Price')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Rooms_Images/', verbose_name='Upload Image for Rooms Section')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Rooms Rates Section',
                'verbose_name_plural': 'Rooms Rates Section',
            },
        ),
    ]
